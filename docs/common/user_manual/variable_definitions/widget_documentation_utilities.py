import argparse
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class InputItem:
    input_item_name_in_json_file: str
    input_item_display_name: str
    input_item_optional: str
    input_item_data_type: str
    input_item_constraints: str
    seealso_text: str
    seealso_link: str
    seealso_description: str


def _make_page_title(title_text: str) -> str:
    return "".join([title_text, "\n", "=" * len(title_text), "\n\n"])


def _make_link_target_string(
    widget_name: str, input_item_name_in_json_file: str
):
    return f".. _{widget_name}_{input_item_name_in_json_file}:\n"


def _make_first_line_of_definition_list_item(
    input_item_display_name: str,
    input_item_optional: str,
    input_item_data_type: str,
):
    term_string = f"{input_item_display_name}"
    if not pd.isnull(input_item_optional):
        classifier_string = f"*{input_item_data_type}, optional*"
    else:
        classifier_string = f"*{input_item_data_type}*"
    return " : ".join([term_string, classifier_string])


def _make_following_lines_of_definition_list_item(
    input_item_description: str,
    input_item_default_value: str,
    input_item_constraints: str,
    input_item_name_in_json_file: str,
):
    definition_string_list = [f"\t{input_item_description}"]
    if not pd.isnull(input_item_default_value):
        definition_string_list.append(f"Default: {input_item_default_value}")
    if not pd.isnull(input_item_constraints):
        definition_string_list.append(f"Constraints: {input_item_constraints}")
    definition_string_list.append(
        f"Key in JSON file: {input_item_name_in_json_file}\n"
    )
    return "\n\n\t".join(definition_string_list)


def _make_definition_list_item_from_parameter_data(
    widget_name: str,
    input_item_name_in_json_file: str,
    input_item_display_name: str,
    input_item_optional: str,
    input_item_data_type: str,
    input_item_description: str,
    input_item_default_value: str,
    input_item_constraints: str,
):
    link_target_string = _make_link_target_string(
        widget_name, input_item_name_in_json_file
    )
    first_line_of_definition_item = _make_first_line_of_definition_list_item(
        input_item_display_name, input_item_optional, input_item_data_type
    )
    following_lines_of_definition_item = (
        _make_following_lines_of_definition_list_item(
            input_item_description,
            input_item_default_value,
            input_item_constraints,
            input_item_name_in_json_file,
        )
    )
    return "\n".join(
        [
            link_target_string,
            first_line_of_definition_item,
            following_lines_of_definition_item,
        ]
    )


def _make_seealso_beginning():
    string = "\n\n.. seealso::\n\n"
    return string


def _make_link_reference_string(text: str, uri: str):
    if uri.lower().startswith("http"):
        link = f"\t`{text} <{uri}>`_\n"
    else:
        link = f"\t:ref:`{text} <{uri}>`\n"
    return link


def _make_seealso(row: InputItem):
    string = _make_link_reference_string(row.seealso_text, row.seealso_link)
    if not pd.isnull(row.seealso_description):
        string += f"\t\t{row.seealso_description}\n"
    return string


def _make_list_of_strings_for_rst_definition_list(
    widget_name: str, widget_data: pd.DataFrame
):
    list_of_strings_definition_list = []
    for row in widget_data.itertuples():
        if not pd.isnull(row.name):
            list_of_strings_definition_list.append(
                _make_definition_list_item_from_parameter_data(
                    widget_name,
                    row.name,
                    row.display_name,
                    row.optional,
                    row.data_type,
                    row.description,
                    row.default_value,
                    row.constraints,
                )
            )
    return list_of_strings_definition_list


def _make_list_of_strings_for_rst_seealso(widget_data: pd.DataFrame):
    list_of_strings_seealso = []
    for row in widget_data.itertuples():
        if not pd.isnull(row.seealso_text):
            list_of_strings_seealso.append(_make_seealso(row))
    return list_of_strings_seealso


def make_rst_file_for_widget(
    rst_file_path: Path, widget_name: str, widget_data: pd.DataFrame
):
    list_of_strings_definition_list = (
        _make_list_of_strings_for_rst_definition_list(widget_name, widget_data)
    )
    list_of_strings_seealso = _make_list_of_strings_for_rst_seealso(
        widget_data
    )
    with open(rst_file_path, "w+") as f:
        f.write(_make_page_title(widget_name))
        f.write("\n\n".join(list_of_strings_definition_list))
        f.write(_make_seealso_beginning())
        f.write("\n".join(list_of_strings_seealso))
        f.write("\n\n\n")


def main(
    csv_files_directory: Path,
    rst_files_directory: Path,
    toc_include_file_path: Path,
    all_data: dict[str, pd.DataFrame],
):
    print(f"Walking through {csv_files_directory}")
    print(f"Creating rst files in {rst_files_directory}")
    print(
        f"Building the file '{toc_include_file_path}' that appropriately includes the generated rst files"
    )

    rst_file_path_list = []
    for widget_name in all_data.keys():
        widget_data = all_data[widget_name]
        csv_file_path = csv_files_directory / f"{widget_name}.csv"
        widget_data.to_csv(csv_file_path)
        rst_file_path = rst_files_directory / f"{widget_name}.rst"
        rst_file_path_list.append(rst_file_path)
        make_rst_file_for_widget(rst_file_path, widget_name, widget_data)

    rst_file_name = toc_include_file_path
    with open(rst_file_name, "w+") as f:
        f.write(_make_page_title("User Inputs"))
        f.write(
            "\n".join(
                [
                    ".. toctree::",
                    "   :maxdepth: 2",
                    "   :caption: User Inputs:",
                    "\n",
                ]
            )
        )
        for rst_file in rst_file_path_list:
            f.write(f"\n   {rst_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate rst files documenting user inputs in SimCenter graphical user interface widgets."
    )
    parser.add_argument(
        "path_to_csv_files",
        help="directory containing csv files defining user inputs",
        type=Path,
    )
    parser.add_argument(
        "--relative_path_to_rst_files",
        help="directory where rst files for widget documentation should be written, the path to this directory is specified relative to the directory containing this python script",
        default="Widget_RST_Files",
        type=Path,
    )
    parser.add_argument(
        "--toc_include_file_path",
        help="path to the file that is included in the table of contents of the SimCenter application documentation",
        default="WidgetTables.rst",
        type=Path,
    )

    command_line_arguments = parser.parse_args()
    csv_files_directory = command_line_arguments.path_to_csv_files.resolve()
    rst_files_directory = (
        command_line_arguments.relative_path_to_rst_files.resolve()
    )
    toc_include_file_path = (
        command_line_arguments.toc_include_file_path.resolve()
    )

    try:
        csv_files_directory.is_dir()
    except:
        raise
    else:
        if not csv_files_directory.is_dir():
            raise OSError(
                f"Specified source directory '{csv_files_directory}' does not exist"
            )

    if not rst_files_directory.is_relative_to(Path(__file__).parent):
        raise ValueError(
            f"Expected a directory that is relative to the parent of this python script, i.e., {Path(__file__).parent}"
        )

    if not rst_files_directory.is_dir():
        rst_files_directory.mkdir(parents=True)

    spreadsheet = "WidgetParameters.xlsx"
    all_data = pd.read_excel(spreadsheet, sheet_name=None)
    main(
        csv_files_directory=csv_files_directory,
        rst_files_directory=rst_files_directory.relative_to(
            Path(__file__).parent
        ),
        toc_include_file_path=toc_include_file_path,
        all_data=all_data,
    )

    print(all_data.keys())
    print("Done!")
