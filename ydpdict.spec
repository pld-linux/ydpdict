Summary:	Fronted to Collins Dictionary
Summary(pl.UTF-8):	Interfejs do słownika Collinsa
Name:		ydpdict
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://toxygen.net/ydpdict/%{name}-%{version}.tar.gz
# Source0-md5:	228ef3d3b1266d76e092e47a1d9535bf
Source1:	%{name}-pl-en.desktop
Source2:	%{name}-en-pl.desktop
Source3:	%{name}.png
URL:		http://toxygen.net/ydpdict/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fronted to Collins Dictionary.

%description -l pl.UTF-8
Program ten pozwala przeglądać słownik Collinsa, wydany przez Young
Digital Poland. Dostępne są słowniki: angielsko-polski,
polsko-angielski, niemiecko-polski oraz polsko-niemiecki.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/{,pl/}man1} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_datadir}/%{name}}

install src/ydpdict $RPM_BUILD_ROOT%{_bindir}
ln -sf ydpdict $RPM_BUILD_ROOT%{_bindir}/ydp
install ydpdict.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/ydpdict.conf
install ydpdict.pl.man $RPM_BUILD_ROOT%{_mandir}/pl/man1/ydpdict.1
install ydpdict.man $RPM_BUILD_ROOT%{_mandir}/man1/ydpdict.1

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ydpdict.conf
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%dir %{_datadir}/ydpdict
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
