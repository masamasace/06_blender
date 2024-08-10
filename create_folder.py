from pathlib import Path

# create sub-directory by referring 1536x768_h1 of 1536x768_h1_0008.png

output_dir = Path("output").resolve()
output_mod_dir = output_dir.parent / "output_mod"

# create sub-directory
sub_dir_str = output_dir.glob("**/*.png")
sub_dir_str = set([str(p.stem[:-5]) for p in sub_dir_str])

for sub_dir in sub_dir_str:
    (output_mod_dir / sub_dir).mkdir(parents=True, exist_ok=True)

# copy png files to sub-directory
for png_file in output_dir.glob("**/*.png"):
    sub_dir = str(png_file.stem[:-5])
    png_file.replace(output_mod_dir / sub_dir / png_file.name)

