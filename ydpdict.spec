Summary:	Fronted to Collins Dictionary
Summary(pl):	Interfejs do s³ownika Collinsa
Name:		ydpdict
Version:	0.63
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://toxygen.net/ydpdict/%{name}-%{version}.tar.gz
# Source0-md5:	bd20edfa221ecb5f04ce6a36b1b15179
Source1:	%{name}-pl-en.desktop
Source2:	%{name}-en-pl.desktop
Source3:	%{name}.png
Patch0:		%{name}-no_local.patch
URL:		http://toxygen.net/ydpdict/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fronted to Collins Dictionary.

%description -l pl
Program ten pozwala przegl±daæ s³ownik Collinsa, wydany przez Young
Digital Poland. Dostêpne s± s³owniki: angielsko-polski,
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
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_datadir}/%{name}}

install src/ydpdict $RPM_BUILD_ROOT%{_bindir}
ln -sf ydpdict $RPM_BUILD_ROOT%{_bindir}/ydp
install ydpdict.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/ydpdict.conf

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%config %verify(not md5 size mtime) %{_sysconfdir}/ydpdict.conf
%{_desktopdir}/*
%{_pixmapsdir}/*
%dir %{_datadir}/ydpdict
