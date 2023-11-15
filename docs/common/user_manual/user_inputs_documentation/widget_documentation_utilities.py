import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DocumentationForUserInputItem:
    key_in_json_file: str
    label_in_user_interface: str
    data_type: str
    description: str
    optional: str
    default_value: str
    constraints: str
    seealso_text: str
    seealso_link: str
    seealso_description: str


class CommandLineArguments:
    path_to_csv_files: Path
    relative_path_to_rst_files: Path
    toc_include_file_path: Path


def _top_level_string() -> str:
    return "User Inputs"


def _make_page_title(title_text: str) -> str:
    return "".join([title_text, "\n", "=" * len(title_text), "\n\n"])


def _make_link_target_string(
    widget_name: str,
    second_string: str,
) -> str:
    return f"\n.. _{widget_name} {second_string}:\n"


def _is_not_blank(string: str) -> bool:
    return bool(string.strip())


def _make_first_line_of_definition_list_item(
    input_item_display_name: str,
    input_item_optional: str,
    input_item_data_type: str,
) -> str:
    term_string = f"{input_item_display_name}"
    if _is_not_blank(input_item_optional):
        classifier_string = f"*{input_item_data_type}, optional*"
    else:
        classifier_string = f"*{input_item_data_type}*"
    return " : ".join([term_string, classifier_string])


def _make_subsequent_lines_of_definition_list_item(
    input_item_description: str,
    input_item_default_value: str,
    input_item_constraints: str,
    input_item_name_in_json_file: str,
) -> str:
    definition_string_list = [f"\t{input_item_description}"]
    if _is_not_blank(input_item_default_value):
        definition_string_list.append(f"Default: {input_item_default_value}")
    if _is_not_blank(input_item_constraints):
        definition_string_list.append(f"Constraints: {input_item_constraints}")
    definition_string_list.append(
        f"Key in JSON file: {input_item_name_in_json_file}\n"
    )
    return "\n\n\t".join(definition_string_list)


def _make_definition_list_item_from_parameter_data(
    widget_name: str,
    input_item: DocumentationForUserInputItem,
) -> str:
    link_target_string = _make_link_target_string(
        widget_name, input_item.key_in_json_file
    )
    first_line_of_definition_item = _make_first_line_of_definition_list_item(
        input_item.label_in_user_interface,
        input_item.optional,
        input_item.data_type,
    )
    following_lines_of_definition_item = (
        _make_subsequent_lines_of_definition_list_item(
            input_item.description,
            input_item.default_value,
            input_item.constraints,
            input_item.key_in_json_file,
        )
    )
    return "\n".join(
        [
            link_target_string,
            first_line_of_definition_item,
            following_lines_of_definition_item,
        ]
    )


def _make_seealso_beginning(start_space: str = "") -> str:
    string = f"{start_space}" + ".. seealso::\n"
    return string


def _make_link_reference_string(
    text: str,
    uri: str,
    start_space: str = "\t",
) -> str:
    if uri.lower().startswith("http"):
        link = f"{start_space}" + f"`{text} <{uri}>`_\n"
    else:
        link = f"{start_space}" + f":ref:`{text} <{uri}>`\n"
    return link


def _make_seealso(
    row: DocumentationForUserInputItem,
    start_space: str = "\t",
) -> str:
    string = _make_link_reference_string(
        row.seealso_text, row.seealso_link, start_space=start_space
    )
    if _is_not_blank(row.seealso_description):
        string += f"{start_space}\t" + f"{row.seealso_description}\n"
    return string


def _make_rst_file_for_widget(
    rst_file_path: Path,
    widget_name: str,
    widget_data: list[DocumentationForUserInputItem],
) -> None:
    list_of_strings_definition_list = []
    list_of_strings_seealso = []
    list_of_strings_seealso.append("\n")
    list_of_strings_seealso.append(_make_seealso_beginning())
    include_see_also = False
    for input_item in widget_data:
        if _is_not_blank(input_item.key_in_json_file):
            list_of_strings_definition_list.append(
                _make_definition_list_item_from_parameter_data(
                    widget_name, input_item
                )
            )
            if _is_not_blank(input_item.seealso_text):
                list_of_strings_definition_list.append(
                    _make_seealso_beginning(start_space="\t")
                )
                list_of_strings_definition_list.append(
                    _make_seealso(input_item, start_space="\t\t")
                )
        else:
            if _is_not_blank(input_item.seealso_text):
                include_see_also = True
                list_of_strings_seealso.append(_make_seealso(input_item))

    with open(rst_file_path, "w+") as f:
        f.write(_make_link_target_string(widget_name, _top_level_string()))
        f.write("\n")
        f.write(_make_page_title(widget_name))
        f.write("\n".join(list_of_strings_definition_list))
        if include_see_also:
            f.write("\n".join(list_of_strings_seealso))
        f.write("\n\n\n")


def _read_one_csv_file(
    csv_file_name: Path,
) -> list[DocumentationForUserInputItem]:
    widget_data = []
    with open(csv_file_name, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            widget_data.append(DocumentationForUserInputItem(**row))
    return widget_data


def _read_widget_documentation_from_csv_files(
    csv_files_directory: Path,
) -> dict[str, list[DocumentationForUserInputItem]]:
    all_widget_documentation_data = {}
    for csv_file_name in csv_files_directory.glob("*.csv"):
        widget_documentation_data = _read_one_csv_file(csv_file_name)
        widget_name = f"{csv_file_name.stem}"
        all_widget_documentation_data[widget_name] = widget_documentation_data
    return all_widget_documentation_data


def _create_rst_files(
    rst_files_directory_path: Path,
    all_widget_documentation_data: dict[
        str,
        list[DocumentationForUserInputItem],
    ],
) -> list[Path]:
    if not (rst_files_directory_path.is_dir()):
        rst_files_directory_path.mkdir(parents=True)
    rst_file_path_list = []
    widget_names = all_widget_documentation_data.keys()
    for widget_name in widget_names:
        widget_documentation_data = all_widget_documentation_data[widget_name]
        rst_file_path = rst_files_directory_path / f"{widget_name}.rst"
        rst_file_path_list.append(rst_file_path)
        _make_rst_file_for_widget(
            rst_file_path, widget_name, widget_documentation_data
        )
    return rst_file_path_list


def _create_toc_include_file(
    toc_include_file_path: Path,
    rst_file_path_list: list[Path],
) -> None:
    with open(toc_include_file_path, "w+") as f:
        f.write(_make_page_title(_top_level_string()))
        f.write(
            "The following pages define the inputs to be provided by users in "
            "the graphical interface of SimCenter applications\n\n"
        )
        f.write(
            "\n".join(
                [
                    ".. toctree::",
                    "   :maxdepth: 2",
                    "   :caption: Definition of User Inputs\n",
                ]
            )
        )
        for rst_file_path in rst_file_path_list:
            f.write(
                f"\n   {rst_file_path.relative_to(rst_file_path.parent.parent)}"
            )


def main(
    csv_files_directory_path: Path,
    rst_files_directory_path: Path,
    toc_include_file_path: Path,
) -> None:
    print(
        "\nINFO: Reading user interface widget documentation "
        f"from csv files in '{csv_files_directory_path}'."
    )
    all_widget_documentation_data = _read_widget_documentation_from_csv_files(
        csv_files_directory_path
    )

    print(f"\nINFO: Creating rst files in '{rst_files_directory_path}'.")
    rst_file_path_list = _create_rst_files(
        rst_files_directory_path, all_widget_documentation_data
    )

    print(
        f"\nINFO: Building the file '{toc_include_file_path}' that includes "
        "the created rst files."
    )
    _create_toc_include_file(toc_include_file_path, rst_file_path_list)
    print(
        f"\n\nNOTE: Ensure that the relative path to '{toc_include_file_path}'"
        " is added to the table of contents of the tool documentation."
    )


def _check_path_to_csv_files(csv_files_directory: Path) -> None:
    try:
        csv_files_directory.is_dir()
    except:
        raise
    else:
        if not csv_files_directory.is_dir():
            raise OSError(
                f"Specified source directory '{csv_files_directory}' does not"
                " exist"
            )


def _handle_arguments(command_line_arguments: CommandLineArguments):
    csv_files_directory = command_line_arguments.path_to_csv_files
    _check_path_to_csv_files(csv_files_directory)

    rst_files_directory = command_line_arguments.relative_path_to_rst_files

    toc_include_file_path = command_line_arguments.toc_include_file_path
    return csv_files_directory, rst_files_directory, toc_include_file_path


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate rst files documenting user inputs in SimCenter graphical"
            " user interface widgets."
        )
    )
    parser.add_argument(
        "path_to_csv_files",
        help="directory containing csv files defining user inputs",
        type=Path,
    )
    parser.add_argument(
        "-r",
        "--relative_path_to_rst_files",
        help=(
            "directory where rst files for widget documentation should be"
            " written, the path to this directory is specified relative to the"
            " directory containing this python script"
        ),
        default="User_Inputs_Documentation_RST_Files",
        type=Path,
    )
    parser.add_argument(
        "-t",
        "--toc_include_file_path",
        help=(
            "path to the file that is included in the table of contents of the"
            " SimCenter application documentation"
        ),
        default="User_Input_Documentation_Tables.rst",
        type=Path,
    )
    return parser


def _print_start_message():
    msg = f"'{Path(__file__).name}' started running"
    print()
    print("=" * len(msg))
    print(msg)
    print()


def _print_end_message():
    msg = f"'{Path(__file__).name}' finished running"
    print()
    print(msg)
    print("=" * len(msg))


if __name__ == "__main__":
    _print_start_message()
    parser = _create_parser()
    command_line_arguments = CommandLineArguments()
    parser.parse_args(namespace=command_line_arguments)
    (
        csv_files_directory_path,
        rst_files_directory_path,
        toc_include_file_path,
    ) = _handle_arguments(command_line_arguments)
    main(
        csv_files_directory_path,
        rst_files_directory_path,
        toc_include_file_path,
    )
    _print_end_message()
