Summary:	Fronted to Collins Dictionary
Summary(pl):	Interfejs do s�ownika Collinsa
Name:		ydpdict
Version:	0.60
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://dev.null.pl/pub/%{name}-%{version}.tar.gz
# Source0-md5:	c55e64aa4e9d16ebb672b840b6ab17c9
Source1:	%{name}-pl-en.desktop
Source2:	%{name}-en-pl.desktop
Source3:	%{name}.png
Patch0:		%{name}-no_local.patch
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fronted to Collins Dictionary.

%description -l pl
Program ten pozwala przegl�da� s�ownik Collinsa, wydany przez Young
Digital Poland. Dost�pne s� s�owniki: angielsko-polski,
polsko-angielski, niemiecko-polski oraz polsko-niemiecki.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Scientific} \
	$RPM_BUILD_ROOT%{_datadir}/ydpdict

install src/ydpdict $RPM_BUILD_ROOT%{_bindir}
ln -sf ydpdict $RPM_BUILD_ROOT%{_bindir}/ydp
install ydpdict.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/ydpdict.conf

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Scientific
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%config %verify(not md5 size mtime) %{_sysconfdir}/ydpdict.conf
%{_applnkdir}/Scientific/*
%{_pixmapsdir}/*
%dir %{_datadir}/ydpdict
