Summary:	Fronted to Collins Dictionary
Summary(pl):	Interfejs do s³ownika Collinsa
Name:		ydpdict
Version:	0.51
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	ftp://amba.bydg.pdi.net/pub/people/wojtekka/%{name}-%{version}.tar.gz
Source1:	%{name}-pl-en.desktop
Source2:	%{name}-en-pl.desktop
Source3:	%{name}.png
Patch0:		%{name}-term.patch
Patch1:		%{name}-segv.patch
Patch2:		%{name}-change_dict.patch
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
%patch1 -p1
%patch2 -p1

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Science}

install ydpdict $RPM_BUILD_ROOT%{_bindir}
ln -sf ydpdict $RPM_BUILD_ROOT%{_bindir}/ydp
install ydpdict.conf $RPM_BUILD_ROOT%{_sysconfdir}

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Science
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%config %verify(not md5 size mtime) %{_sysconfdir}/ydpdict.conf
%{_applnkdir}/Science/*
%{_pixmapsdir}/*
