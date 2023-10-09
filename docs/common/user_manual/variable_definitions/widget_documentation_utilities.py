import os
import pandas as pd


def _make_page_title(title_text):
    return ("".join([title_text, "\n", "="*len(title_text), "\n\n"]))


def _make_link_target_string(row, widget_name):
    return f'.. _{"".join(widget_name.strip().split())}_{"".join(row.name.strip().split())}:\n'


def _make_first_line_of_definition_list_item(row):
    term_string = f"{row.display_name}"
    if not pd.isnull(row.optional):
        classifier_string = f"*{row.data_type}, optional*"
    else:
        classifier_string = f"*{row.data_type}*"
    return " : ".join([term_string, classifier_string])


def _make_following_lines_of_definition_list_item(row):
    definition_string_list = [f"\t{row.description}"]
    if not pd.isnull(row.default_value):
        definition_string_list.append(f"Default: {row.default_value}")
    if not pd.isnull(row.constraints):
        definition_string_list.append(f"Constraints: {row.constraints}")
    definition_string_list.append(f"Key in JSON file: {row.name}\n")
    return "\n\n\t".join(definition_string_list)


def _make_definition_list_item_from_parameter_data(row, widget_name):
    link_target_string = _make_link_target_string(row, widget_name)
    first_line_of_definition_item = _make_first_line_of_definition_list_item(row)
    following_lines_of_definition_item = _make_following_lines_of_definition_list_item(row)
    return "\n".join([link_target_string, first_line_of_definition_item, following_lines_of_definition_item])


def _make_seealso_beginning():
    string = "\n\n.. seealso::\n\n"
    return string


def _make_link_reference_string(text, uri):
    if uri.lower().startswith("http"):
        link = f"\t`{text} <{uri}>`_\n"
    else:
        link = f"\t:ref:`{text} <{uri}>`\n"
    return link


def _make_seealso(row):
    string = _make_link_reference_string(row.seealso_text, row.seealso_link)
    if not pd.isnull(row.seealso_description):
        string += f"\t\t{row.seealso_description}\n"
    return string


def _make_list_of_strings_for_rst_definition_list(widget_name, widget_data):
    list_of_strings_definition_list = []
    for row in widget_data.itertuples():
        if not pd.isnull(row.name):
            list_of_strings_definition_list.append(_make_definition_list_item_from_parameter_data(row, widget_name))
    return list_of_strings_definition_list


def _make_list_of_strings_for_rst_seealso(widget_data):
    list_of_strings_seealso = []
    for row in widget_data.itertuples():
        if not pd.isnull(row.seealso_text):
            list_of_strings_seealso.append(_make_seealso(row))
    return list_of_strings_seealso


def make_rst_file_for_widget(rst_file_path, widget_name, widget_data):
    list_of_strings_definition_list = _make_list_of_strings_for_rst_definition_list(widget_name, widget_data)
    list_of_strings_seealso = _make_list_of_strings_for_rst_seealso(widget_data)
    with open(rst_file_path, "w+") as f:
        f.write(_make_page_title(widget_name))
        f.write("\n\n".join(list_of_strings_definition_list))
        f.write(_make_seealso_beginning())
        f.write("\n".join(list_of_strings_seealso))
        f.write("\n\n\n")


def main(csv_files_directory, rst_files_directory, all_data):
    rst_file_path_list = []
    for widget_name in all_data.keys():
        widget_data = all_data[widget_name]
        csv_file_path = os.path.join(csv_files_directory, f"{widget_name}.csv")
        widget_data.to_csv(csv_file_path)
        rst_file_path = os.path.join(rst_files_directory, f"{widget_name}.rst")
        rst_file_path_list.append(rst_file_path)
        make_rst_file_for_widget(rst_file_path, widget_name, widget_data)
        
    rst_file_name = "WidgetTables.rst"
    with open(rst_file_name, "w+") as f:
        f.write(_make_page_title("User Defined Inputs"))
        f.write("\n".join([".. toctree::",
                        "   :maxdepth: 2",
                        "   :caption: User Defined Inputs:",
                        "\n"]))
        for rst_file in rst_file_path_list:
            f.write(f"\n   {rst_file}")


if __name__=="__main__":
    spreadsheet = "WidgetParameters.xlsx"
    all_data = pd.read_excel(spreadsheet, sheet_name=None)

    csv_files_directory = "Widget_CSV_Files"
    rst_files_directory = "Widget_RST_Files"
    if not os.path.exists(csv_files_directory):
        os.mkdir(csv_files_directory)
    if not os.path.exists(rst_files_directory):
        os.mkdir(rst_files_directory)
    
    main(csv_files_directory=csv_files_directory, rst_files_directory=rst_files_directory, all_data=all_data)

    print(all_data.keys())
    print("Done!")
