Summary:	WINGs based graphical front-end for APT
Summary(es):	Front-end grafico para APT
Summary(pl):	Bazuj±cy na WING graficzny interfejs do APTa
Summary(pt_BR):	Front-end gráfico para APT baseado em WINGs
Name:		synaptic
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	ftp://ftp.conectiva.com/pub/conectiva/EXPERIMENTAL/synaptic/%{name}-%{version}.tar.gz
URL:		http://distro.conectiva.com/projetos/46/
BuildRequires:	apt-devel >= 0.3.19cnc36
BuildRequires:	WindowMaker-devel >= 0.65.0
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Synaptic is a graphical front-end for APT (Advanced Package Tool)
written with the Window Maker toolkit. It attempts to be a lot easier
to use than other existing APT front-ends.

Instead of using trees to display packages, Synaptic is heavily based
on a powerful package filtering system. That greatly simplifies the
interface while giving a lot more flexibility to browse through very
long package lists.

%description -l es
Synaptic is a graphical front-end for APT (Advanced Package Tool)
written with the Window Maker toolkit. It attempts to be a lot easier
to use than other existing APT front-ends.

Instead of using trees to display packages, Synaptic is heavily based
on a powerful package filtering system. That greatly simplifies the
interface while giving a lot more flexibility to browse through very
long package lists.

%description -l pl
Synaptic jest graficznym frontendem dla APT napisany z u¿yciem
toolkita WindowMakera. Synaptic próbuje byæ ³atwiejszym w u¿yciu ni¿
inne istniej±ce frontendy dla APT.

Zamiast u¿ywaj±c drzew do wy¶wietlania pakietów, Synaptic mocno bazuje
na systemie filtrowania pakietów o ogromnych mo¿liwo¶ciach. To w
ogromnym stopniu upraszcza interfejs równocze¶nie daj±c znacznie
wiêksz± elastyczno¶æ podczas przegl±dania d³ugich list pakietów.

%description -l pt_BR
Synaptic é um front-end gráfico para o APT (Advanced Package Tool)
escrito com o toolkit do Window Maker. Seu objetivo é ser mais fácil
de usar que outros front-ends do APT.

Em vez de utilizar estruturas em árvore para mostrar os pacotes,
Synaptic utiliza um sistema de filtro de pacotes, simplificando a
interface e oferecendo mais flexibilidade quando houver um grande
numero de pacotes listado.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/
install -D -m755 src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D help.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/help.txt
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
cd po
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}
cd ..

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS INSTALL NEWS README TODO %{name}-hackers-guide.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/help.txt
%{_localstatedir}/lib/%{name}
