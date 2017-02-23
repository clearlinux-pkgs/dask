#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dask
Version  : 0.13.0
Release  : 1
URL      : https://pypi.python.org/packages/8a/f2/803cbcd073db393b846a518e87892c3610659bfc7b9689d99a0fd0fa63b5/dask-0.13.0.tar.gz
Source0  : https://pypi.python.org/packages/8a/f2/803cbcd073db393b846a518e87892c3610659bfc7b9689d99a0fd0fa63b5/dask-0.13.0.tar.gz
Summary  : Parallel PyData with Task Scheduling
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dask-python
Requires: numpy
Requires: pandas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Dask
====
|Build Status| |Coverage| |Doc Status| |Gitter| |Version Status|
Dask is a flexible parallel computing library for analytics.  See
documentation_ for more information.

%package python
Summary: python components for the dask package.
Group: Default

%description python
python components for the dask package.


%prep
%setup -q -n dask-0.13.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487880052
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487880052
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
