Summary:      Fronted to Collins Dictionary
Summary(pl):  Interfejs do s�ownika Collinsa
Name:         ydpdict
Version:      0.51
Release:      1
Copyright:    GPL
Group:        Utilities/Text
Group(pl):    Narz�dzia/Tekst
Source0:      ftp://amba.bydg.pdi.net/pub/people/wojtekka/%{name}-%{version}.tar.gz
Patch0:       %{name}-term.patch
Requires:     ncurses
BuildRoot:    %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fronted to Collins Dictionary

%description -l pl
Program ten pozwala przegl�da� angielsko-polski i polsko-angielski s�ownik
Collinsa, wydany przez Young Digital Poland.

%prep
%setup
%patch0 -p1

%build
make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_sysconfdir}}
install -s ydpdict $RPM_BUILD_ROOT%{_bindir}/ydpdict
install ydpdict $RPM_BUILD_ROOT%{_bindir}
install ydpdict.conf $RPM_BUILD_ROOT%{_sysconfdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)                                                                           
%attr(755,root,root) %{_bindir}/ydpdict
%config %{_sysconfdir}/ydpdict.conf
