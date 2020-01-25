# NOTE: for versions >= 0.7.0 (for python 3.4+) see python3-pyxattr.spec
#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_with	python3	# CPython 3.x module

%define 	module	pyxattr
Summary:	Python 2 module for accessing Extended Attributes of the files
Summary(pl.UTF-8):	Moduł Pythona 2 pozwalający na dostęp do rozszerzonych atrybutów plików
Name:		python-%{module}
# note: keep 0.6.x here (python 2 support dropped in 0.7.x)
Version:	0.6.1
Release:	2
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://pyxattr.k1024.org/downloads/%{module}-%{version}.tar.gz
# Source0-md5:	523e9d90f9801141c785d93e6197cc33
URL:		https://pyxattr.k1024.org/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 module for accessing Extended Attributes of the files.

%description -l pl.UTF-8
Moduł Pythona 2 pozwalający na dostęp do rozszerzonych atrybutów
plików.

%package -n python3-%{module}
Summary:	Python 3 module for accessing Extended Attributes of the files
Summary(pl.UTF-8):	Moduł Pythona 3 pozwalający na dostęp do rozszerzonych atrybutów plików
Group:		Libraries/Python

%description -n python3-%{module}
Python 3 module for accessing Extended Attributes of the files.

%description -n python3-%{module} -l pl.UTF-8
Moduł Pythona 3 pozwalający na dostęp do rozszerzonych atrybutów
plików.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%attr(755,root,root) %{py_sitedir}/xattr.so
%{py_sitedir}/pyxattr-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/xattr.cpython-*.so
%{py3_sitedir}/pyxattr-%{version}-py*.egg-info
%endif
