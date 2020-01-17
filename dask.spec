#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dask
Version  : 2.9.2
Release  : 77
URL      : https://files.pythonhosted.org/packages/e4/59/2a82b72fede7e00cfa13b1fcf31c4f20251cbb3d427b491cb0260b663811/dask-2.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/59/2a82b72fede7e00cfa13b1fcf31c4f20251cbb3d427b491cb0260b663811/dask-2.9.2.tar.gz
Summary  : Parallel PyData with Task Scheduling
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dask-license = %{version}-%{release}
Requires: dask-python = %{version}-%{release}
Requires: dask-python3 = %{version}-%{release}
Requires: bokeh
Requires: cloudpickle
Requires: distributed
Requires: numpy
Requires: pandas
Requires: partd
Requires: toolz
BuildRequires : bokeh
BuildRequires : buildreq-distutils3
BuildRequires : cloudpickle
BuildRequires : distributed
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : partd
BuildRequires : pytest-runner
BuildRequires : toolz

%description
Dask
====
|Build Status| |Coverage| |Doc Status| |Gitter| |Version Status| |NumFOCUS|

%package license
Summary: license components for the dask package.
Group: Default

%description license
license components for the dask package.


%package python
Summary: python components for the dask package.
Group: Default
Requires: dask-python3 = %{version}-%{release}

%description python
python components for the dask package.


%package python3
Summary: python3 components for the dask package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dask package.


%prep
%setup -q -n dask-2.9.2
cd %{_builddir}/dask-2.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579274804
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dask
cp %{_builddir}/dask-2.9.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/dask/98e42a13a272323dc03ebff615190ec2dba9c484
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dask/98e42a13a272323dc03ebff615190ec2dba9c484

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
