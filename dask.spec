#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dask
Version  : 0.18.2
Release  : 38
URL      : http://pypi.debian.net/dask/dask-0.18.2.tar.gz
Source0  : http://pypi.debian.net/dask/dask-0.18.2.tar.gz
Summary  : Parallel PyData with Task Scheduling
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dask-python3
Requires: dask-license
Requires: dask-python
Requires: cloudpickle
Requires: numpy
Requires: pandas
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest-runner
BuildRequires : python3-dev
BuildRequires : setuptools

%description
====
        
        |Build Status| |Coverage| |Doc Status| |Gitter| |Version Status|
        
        Dask is a flexible parallel computing library for analytics.  See
        documentation_ for more information.
        
        
        LICENSE
        -------

%package license
Summary: license components for the dask package.
Group: Default

%description license
license components for the dask package.


%package python
Summary: python components for the dask package.
Group: Default
Requires: dask-python3

%description python
python components for the dask package.


%package python3
Summary: python3 components for the dask package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dask package.


%prep
%setup -q -n dask-0.18.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532361725
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/dask
cp LICENSE.txt %{buildroot}/usr/share/doc/dask/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/dask/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
