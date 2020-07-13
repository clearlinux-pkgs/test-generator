#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : test-generator
Version  : 0.1.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/1e/b3/90a71f2f4f9de5467c5518f0d75876eb7501c07fa1e25353ceaa56da3973/test-generator-0.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/1e/b3/90a71f2f4f9de5467c5518f0d75876eb7501c07fa1e25353ceaa56da3973/test-generator-0.1.2.tar.gz
Summary  : Generator is a helper for generating test methods for nose while still using unittest
Group    : Development/Tools
License  : HPND ISC
Requires: test-generator-license = %{version}-%{release}
Requires: test-generator-python = %{version}-%{release}
Requires: test-generator-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : six
BuildRequires : six-python

%description
Generator
        ===============================

%package license
Summary: license components for the test-generator package.
Group: Default

%description license
license components for the test-generator package.


%package python
Summary: python components for the test-generator package.
Group: Default
Requires: test-generator-python3 = %{version}-%{release}

%description python
python components for the test-generator package.


%package python3
Summary: python3 components for the test-generator package.
Group: Default
Requires: python3-core
Provides: pypi(test_generator)
Requires: pypi(six)

%description python3
python3 components for the test-generator package.


%prep
%setup -q -n test-generator-0.1.2
cd %{_builddir}/test-generator-0.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583698130
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/test-generator
cp %{_builddir}/test-generator-0.1.2/LICENSE %{buildroot}/usr/share/package-licenses/test-generator/75a3c6d489d6c7addb504840691981a8f5314442
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/test-generator/75a3c6d489d6c7addb504840691981a8f5314442

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
