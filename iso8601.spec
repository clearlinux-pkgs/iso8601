#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iso8601
Version  : 0.1.11
Release  : 18
URL      : https://pypi.python.org/packages/source/i/iso8601/iso8601-0.1.11.tar.gz
Source0  : https://pypi.python.org/packages/source/i/iso8601/iso8601-0.1.11.tar.gz
Summary  : Simple module to parse ISO 8601 dates
Group    : Development/Tools
License  : MIT
Requires: iso8601-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Simple module to parse ISO 8601 dates
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

%package python
Summary: python components for the iso8601 package.
Group: Default

%description python
python components for the iso8601 package.


%prep
%setup -q -n iso8601-0.1.11

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7  --verbose iso8601
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
