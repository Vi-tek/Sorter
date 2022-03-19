import os


def sort(suffixes: tuple, src_path: str, dst_path: str, verbose: bool = False):
    """

    :param suffixes: tuple of file suffixes (mp4, mov)
    :param src_path: path that contains files needed be sorted
    :param dst_path: destination path sorted files
    :param verbose: prints paths to which were files sorted to
    :return: void
    """

    assert suffixes, "List is empty"
    assert os.path.exists(dst_path) and os.path.exists(src_path), "Path does not exist"

    for file in os.listdir(src_path):
        src_p = src_path + file

        if os.path.isfile(src_p):
            dst_p = dst_path + file
            name, suffix = file.rsplit(".", maxsplit=1)
            if suffix in suffixes:
                try:
                    os.rename(src_p, dst_p)
                    if verbose:
                        print("Moved: ", dst_p)
                except FileExistsError:
                    duplicants = len([x for x in os.listdir(dst_path) if name in x])
                    os.rename(src_p, dst_path + name + " (%s)." % duplicants + suffix)
                    if verbose:
                        print("Duplicant: ", dst_path + name + "(%s)" % duplicants + suffix)


sort(suffixes=("mp4", "mov"), src_path="C:\\Users\\", dst_path="C:\\")
