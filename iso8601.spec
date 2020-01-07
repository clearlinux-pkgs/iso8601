#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iso8601
Version  : 0.1.12
Release  : 46
URL      : https://pypi.debian.net/iso8601/iso8601-0.1.12.tar.gz
Source0  : https://pypi.debian.net/iso8601/iso8601-0.1.12.tar.gz
Summary  : Simple module to parse ISO 8601 dates
Group    : Development/Tools
License  : MIT
Requires: iso8601-python3
Requires: iso8601-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
This module parses the most common forms of ISO 8601 date strings (e.g.

%package python
Summary: python components for the iso8601 package.
Group: Default
Requires: iso8601-python3

%description python
python components for the iso8601 package.


%package python3
Summary: python3 components for the iso8601 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the iso8601 package.


%prep
%setup -q -n iso8601-0.1.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523290100
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
