Summary:	Fronted to Collins Dictionary
Summary(pl):	Interfejs do s³ownika Collinsa
Name:		ydpdict
Version:	0.51
Release:	2
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://amba.bydg.pdi.net/pub/people/wojtekka/%{name}-%{version}.tar.gz
Patch0:		%{name}-term.patch
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
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}

install ydpdict $RPM_BUILD_ROOT%{_bindir}
install ydpdict.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ydpdict
%config %verify(not md5 size mtime) %{_sysconfdir}/ydpdict.conf
