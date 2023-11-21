import argparse
import dataclasses
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from widget_documentation_utilities import (
    DocumentationForUserInputItem,
    _is_not_blank,
    _print_end_message,
    _print_start_message,
)


class CommandLineArguments:
    path_to_file_with_widget_names: Path
    path_to_csv_files: Path


def _make_csv_header() -> str:
    field_name_list = []
    for field in dataclasses.fields(DocumentationForUserInputItem):
        field_name_list.append(field.name)
    return ",".join(field_name_list)


def _get_list_of_names_of_widgets_to_be_documented(
    file_with_widget_names: Path,
) -> list[str]:
    set_of_widget_names_to_be_documented = set()
    with open(file_with_widget_names, "r", encoding="utf-8") as f:
        for line in f:
            if _is_not_blank(line):
                line = line.split("\\")[0].strip()
                if not line.startswith("#"):
                    path = Path(line)
                    set_of_widget_names_to_be_documented.add(path.stem)
    return list(set_of_widget_names_to_be_documented)


def _make_one_csv_documentation_starter_file(
    csv_file_name: Path,
    header: str,
):
    with open(csv_file_name, "w") as f:
        f.write(header)
        f.write("\n")
    print(f"STATUS: Created documentation starter file '{csv_file_name}'")


def _make_csv_documentation_starter_files(
    list_of_widget_names_to_be_documented: list[str],
    csv_files_directory_path: Path,
) -> None:
    counter = 0
    header = _make_csv_header()
    for widget_name in list_of_widget_names_to_be_documented:
        csv_file_name = csv_files_directory_path / f"{widget_name}.csv"
        if not csv_file_name.exists():
            csv_file_name.touch()
            _make_one_csv_documentation_starter_file(csv_file_name, header)
            counter += 1
    print(
        f"\nINFO: Created {counter} new csv documentation starter file(s).\n"
    )


def _count_lines_in_file(file_name: str) -> int:
    with open(file_name, "rb") as f:
        num_lines = sum(1 for _ in f)
    return num_lines


def _count_of_documented_widgets(
    csv_files_directory_path: Path,
) -> tuple[int, int]:
    documentation_content_exists_counter = 0
    csv_files_list = list(csv_files_directory_path.glob("*.csv"))
    num_csv_files = len(csv_files_list)
    for csv_file_name in csv_files_list:
        num_lines = _count_lines_in_file(str(csv_file_name))
        if num_lines > 1:
            documentation_content_exists_counter += 1
    return documentation_content_exists_counter, num_csv_files


def main(
    file_with_widget_names: Path,
    csv_files_directory_path: Path,
) -> None:
    list_of_widget_names_to_be_documented = (
        _get_list_of_names_of_widgets_to_be_documented(file_with_widget_names)
    )
    print(
        f"\nINFO: Found {len(list_of_widget_names_to_be_documented)} "
        f"widgets to be documented in '{file_with_widget_names}'.\n"
    )
    _make_csv_documentation_starter_files(
        list_of_widget_names_to_be_documented,
        csv_files_directory_path,
    )
    (
        number_of_documentation_files_with_content,
        total_number_of_documentation_files,
    ) = _count_of_documented_widgets(csv_files_directory_path)
    print(
        f"\nINFO: Found {total_number_of_documentation_files} documentation "
        f"file(s) in '{csv_files_directory_path}' "
        f"out of which {number_of_documentation_files_with_content} file(s) "
        "had some documentation content.\n"
    )


def _handle_arguments(
    command_line_arguments: CommandLineArguments,
) -> tuple[Path, Path]:
    file_with_widget_names = (
        command_line_arguments.path_to_file_with_widget_names
    )
    path_to_csv_files = command_line_arguments.path_to_csv_files
    if not path_to_csv_files.is_dir():
        path_to_csv_files.mkdir(parents=True)
    return file_with_widget_names, path_to_csv_files


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate starter files for documenting user inputs in SimCenter "
            "graphical user interface widgets."
        )
    )
    parser.add_argument(
        "path_to_file_with_widget_names",
        help="file containing names of widgets requiring user inputs",
        type=Path,
    )
    parser.add_argument(
        "-c",
        "--path_to_csv_files",
        help=(
            "directory where csv files for widget documentation will be"
            " written, the path to this directory is specified relative to the"
            " directory containing this python script"
        ),
        default="User_Inputs_Documentation_CSV_File_Templates",
        type=Path,
    )
    return parser


if __name__ == "__main__":
    _print_start_message()
    parser = _create_parser()
    command_line_arguments = CommandLineArguments()
    parser.parse_args(namespace=command_line_arguments)
    (
        file_with_widget_names,
        path_to_csv_files,
    ) = _handle_arguments(
        command_line_arguments,
    )
    main(
        file_with_widget_names,
        path_to_csv_files,
    )
    _print_end_message()
