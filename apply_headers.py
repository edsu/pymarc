#!/usr/bin/env python

"""Apply standard license headers and generate contributor list.

Rather than trying to maintain file-level lists of contributors and copyright
dates, apply a standard license header that points to the LICENSE file for the
licensing details. And then generate the LICENSE file with a complete list of
contributors based on the git commit history.

To adjust contributor names or combine email addresses, see .mailmap.

See https://github.com/edsu/pymarc/issues/147 for context.
"""

# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.

import pathlib
import shlex
import subprocess


def get_contributors():
    """Get a complete list of contributors from `git log`."""
    # dictionary = add each name only once
    contribs = {}

    gitargs = shlex.split("git log --use-mailmap --format=short")
    log = subprocess.run(gitargs, capture_output=True, encoding="utf-8")
    for line in log.stdout.split("\n"):
        if line[0 : len("Author: ")] == "Author: ":
            contribs[line[len("Author: ") :]] = 1

    # Return a list of the contributors
    return sorted(contribs)


def generate_license(contribs):
    """Generate a BSD-2 license file that lists contributors."""
    bsd2 = """Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

    with open("LICENSE", "w") as licensef:
        licensef.write(bsd2)
        licensef.write(
            "Copyright for this project is held by its many contributors, including:\n\n"
        )
        for contrib in contribs:
            licensef.write("{}\n".format(contrib))


def apply_headers():
    """Ensure standard license header is in each Python file."""
    header = """# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.
"""

    path = pathlib.Path(".")
    for pyfile in list(path.glob("**/*.py")):
        if str(pyfile) == "docs/source/conf.py" or str(pyfile) == "test/__init__.py":
            continue
        with open(pyfile, "r") as reader:
            contents = reader.read()
            if contents.find(header) == -1:
                if str(pyfile) == "test/__init__.py":
                    # Avoid angering black with a blank line at the end
                    write_header(pyfile, reader, contents, header)
                else:
                    write_header(pyfile, reader, contents, header + "\n")


def write_header(pyfile, reader, contents, header):
    """Rewrite Python source file with the license header."""
    reader.close()
    utf8_decl = "# -*- coding: utf-8 -*-\n"
    with open(pyfile, "w") as writer:
        if contents.startswith("# __init__.py"):
            sections = contents.split("\n\n", 1)
            writer.write(sections[0])
            writer.write("\n\n")
            writer.write(header)
            writer.write(sections[1])
        elif contents.startswith(utf8_decl):
            sections = contents.split(utf8_decl, 1)
            writer.write(utf8_decl)
            writer.write("\n")
            writer.write(header)
            writer.write(sections[1])
        else:
            writer.write(header)
            writer.write(contents)


if __name__ == "__main__":
    generate_license(get_contributors())
    apply_headers()
