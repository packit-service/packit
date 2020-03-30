from tests.spellbook import (
    TARBALL_NAME,
    git_add_and_commit,
    build_srpm,
    create_merge_commit_in_source_git,
)
    spec = Specfile(distgit / "beer.spec")
    spec = Specfile(distgit / "beer.spec")
    create_merge_commit_in_source_git(sourcegit)

        """
-Version:        0.0.0
+Version:        0.1.0"""
        in git_diff
    )

    assert (
        """
+# PATCHES FROM SOURCE GIT:
+
+# MERGE COMMIT!
+# Author: Packit Test Suite <test@example.com>
+Patch0001: 0-0001-switching-to-amarillo-hops.patch
+
+# MERGE COMMIT!
+# Author: Packit Test Suite <test@example.com>
+Patch0002: 1-0002-actually-let-s-do-citra.patch
+
+# source change
+# Author: Packit Test Suite <test@example.com>
+Patch0003: 2-0001-source-change.patch
+
+
 %description
"""
        in git_diff
    )
    assert "Patch0004:" not in git_diff

    assert (
        """ %prep
-%autosetup -n %{upstream_name}-%{version}
+%autosetup -p1 -n %{upstream_name}-%{version}"""
        in git_diff
    )

    assert (
        """ - 0.1.0-1
+- new upstream release: 0.1.0
+
 * Sun Feb 24 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.0.0-1
 - No brewing, yet."""
        in git_diff
        """diff --git a/.packit.yaml b/.packit.yaml
new file mode 100644"""
        in git_diff
    )

    assert (
        """
--- /dev/null
+++ b/.packit.yaml"""
        in git_diff
        """
+diff --git a/.packit.yaml b/.packit.yaml
+new file mode 100644"""
        not in git_diff
        """
+Subject: [PATCH] source change
+
+---
+ big-source-file.txt | 3 +--
+ 1 file changed, 1 insertion(+), 2 deletions(-)
+
+diff --git a/big-source-file.txt b/big-source-file.txt"""
        in git_diff
        "+Subject: [PATCH 2/2] actually, let's do citra\n"
        "+\n"
        "+---\n"
        "+ hops | 2 +-\n"
        "+ 1 file changed, 1 insertion(+), 1 deletion(-)\n"
    ) in git_diff

    assert (
        """
+--- a/big-source-file.txt
++++ b/big-source-file.txt
+@@ -1,2 +1 @@
+-This is a testing file
+-containing some text.
++new changes"""
        in git_diff
        """
--- a/big-source-file.txt
+++ b/big-source-file.txt
@@ -1,2 +1 @@
-This is a testing file
-containing some text.
+new changes"""
        not in git_diff
    create_merge_commit_in_source_git(sg_path)