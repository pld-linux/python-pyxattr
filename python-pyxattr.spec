
%define 	module	pyxattr

Summary:	Python module for accessing Extended Attributes of the files
Summary(pl.UTF-8):	Moduł języka Python pozwalający na dostęp do rozszerzonych atrybutów plików
Name:		python-%{module}
Version:	0.2.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	33d722b0c67fcee42bb3c6455f135f94
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
%doc *.html
%attr(755,root,root) %{py_sitedir}/*.so
