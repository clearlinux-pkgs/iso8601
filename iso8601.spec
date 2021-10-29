#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iso8601
Version  : 0.1.16
Release  : 62
URL      : https://files.pythonhosted.org/packages/45/66/a943f702763c879e2754b46089a136ee1e58f0f720c58fa640c00281d3fd/iso8601-0.1.16.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/66/a943f702763c879e2754b46089a136ee1e58f0f720c58fa640c00281d3fd/iso8601-0.1.16.tar.gz
Summary  : Simple module to parse ISO 8601 dates
Group    : Development/Tools
License  : MIT
Requires: iso8601-license = %{version}-%{release}
Requires: iso8601-python = %{version}-%{release}
Requires: iso8601-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
This module parses the most common forms of ISO 8601 date strings (e.g.

%package license
Summary: license components for the iso8601 package.
Group: Default

%description license
license components for the iso8601 package.


%package python
Summary: python components for the iso8601 package.
Group: Default
Requires: iso8601-python3 = %{version}-%{release}

%description python
python components for the iso8601 package.


%package python3
Summary: python3 components for the iso8601 package.
Group: Default
Requires: python3-core
Provides: pypi(iso8601)

%description python3
python3 components for the iso8601 package.


%prep
%setup -q -n iso8601-0.1.16
cd %{_builddir}/iso8601-0.1.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628728734
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iso8601
cp %{_builddir}/iso8601-0.1.16/LICENSE %{buildroot}/usr/share/package-licenses/iso8601/604d3444602058d69df81bd0c30c6944517360db
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iso8601/604d3444602058d69df81bd0c30c6944517360db

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
