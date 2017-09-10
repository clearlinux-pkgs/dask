#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dask
Version  : 0.15.2
Release  : 9
URL      : http://pypi.debian.net/dask/dask-0.15.2.tar.gz
Source0  : http://pypi.debian.net/dask/dask-0.15.2.tar.gz
Summary  : Parallel PyData with Task Scheduling
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dask-legacypython
Requires: dask-python
Requires: numpy
Requires: pandas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
====
        
        |Build Status| |Coverage| |Doc Status| |Gitter| |Version Status|
        
        Dask is a flexible parallel computing library for analytics.  See
        documentation_ for more information.
        
        
        LICENSE
        -------

%package legacypython
Summary: legacypython components for the dask package.
Group: Default

%description legacypython
legacypython components for the dask package.


%package python
Summary: python components for the dask package.
Group: Default
Requires: dask-legacypython

%description python
python components for the dask package.


%prep
%setup -q -n dask-0.15.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505001747
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505001747
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
