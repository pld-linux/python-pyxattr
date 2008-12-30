
%define 	module	pyxattr

Summary:	Python module for accessing Extended Attributes of the files
Summary(pl.UTF-8):	Moduł języka Python pozwalający na dostęp do rozszerzonych atrybutów plików
Name:		python-%{module}
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	8e54ffa2ca575232d57213efcbcee289
URL:		http://pyxattr.sourceforge.net/
BuildRequires:	attr-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for accessing Extended Attributes of the files.

%description -l pl.UTF-8
Moduł języka Python pozwalający na dostęp do rozszerzonych atrybutów
plików.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/pyxattr-*.egg-info
