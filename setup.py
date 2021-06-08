import cx_Freeze
executable = [cx_Freeze.Executable("archive-org-scraper.py")]
cx_Freeze.setup(
    name = "Archive-org-scraper",
    options={"build_exe": {"packages":["selenium"],
                           "include_files": []}},
                executables = executable
)