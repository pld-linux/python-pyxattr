%include	/usr/lib/rpm/macros.python
%define 	module pyxattr
Summary:	python module for accessing filesystem Extended Attributes
Summary(pl):	modu³ pythona pozwalaj±cy na dostêp Extended Attributes systemu plików
Name:		python-%{module}
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	6f824d05d6052c05f327d619f92c8a5a
URL:		http://pyxattr.sourceforge.net/
BuildRequires:	attr-devel
BuildRequires:	rpm-pythonprov
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python module for accessing filesystem Extended Attributes.

%description -l pl
modu³ pythona pozwalaj±cy na dostêp Extended Attributes systemu plików.

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
