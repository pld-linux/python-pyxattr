%define 	module	pyxattr
Summary:	Python module for accessing Extended Attributes of the files
Summary(pl.UTF-8):	Moduł języka Python pozwalający na dostęp do rozszerzonych atrybutów plików
Name:		python-%{module}
Version:	0.5.0
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyxattr/%{module}-%{version}.tar.gz
# Source0-md5:	0f7ab1e185087329e40f7de218517c84
URL:		http://pyxattr.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	attr-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for accessing Extended Attributes of the files.

%description -l pl.UTF-8
Moduł języka Python pozwalający na dostęp do rozszerzonych atrybutów
plików.

%prep
%setup -q -n %{module}-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/xattr.so
%{py_sitedir}/pyxattr-%{version}-py*.egg-info
