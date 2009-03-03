Summary:	Replayer for old amiga music file formats
Summary(pl.UTF-8):	Odtwarzacz starych amigowych plików muzycznych
Name:		uade2
Version:	2.12
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://zakalwe.virtuaalipalvelin.net/uade/uade2/uade-%{version}.tar.bz2
# Source0-md5:	72342daf52b43ac0c51086cdc088f25c
URL:		http://zakalwe.virtuaalipalvelin.net/uade/
BuildRequires:	gtk+-devel
BuildRequires:	libao-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UADE is a replayer for old amiga music file formats. It uses an UAE
emulation of the AMIGA Hardware and a cloned m68k-assembler Amiga
delitracker API to be able to replay those tunes again on platforms
other than the original AMIGA.

%description -l pl.UTF-8
UADE jest odtwarzaczem starych amigowych formatów plików muzycznych.
Używa emulacji sprzętu z UAE i sklonowanego API delitrackera, by móc
odtworzyć ponownie te melodie na platformach innych niż Amiga.

%package examples
Summary:	Sample amiga tunes
Summary(pl.UTF-8):	Przykładowe melodie
Group:		Applications/Sound

%description examples
Some sample amiga tunes you can use to test if UADE works.

%description examples -l pl.UTF-8
Kilka przykładowych amigowych melodii, które można wykorzystać do
sprawdzenia, czy UADE działa.

%package -n xmms-input-uade2
Summary:	UADE plugin for XMMS
Summary(pl.UTF-8):	Wtyczka dla XMMS-a wykorzystująca UADE
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description -n xmms-input-uade2
For people that prefer a GUI rather than plain console apps and their
switches or those who just want to listen to their music with XMMS and
take advantage of it's features like playlists, different output,
effect and visual plugins there's also a UADE XMMS input plugin.

%description -n xmms-input-uade2 -l pl.UTF-8
Dla tych, którzy preferują GUI od aplikacji trybu tekstowego i ich
przełączników, lub po prostu chcą słuchać muzyki używając XMMS-a,
korzystając z jego cech, takich jak playlisty, różne wyjścia, efekty i
wtyczki wizualizacyjne, jest wtyczka dla XMMS-a korzystająca z UADE.

%prep
%setup -q -n uade-%{version}

%build
./configure \
	--prefix=%{_prefix} \
	--package-prefix=$RPM_BUILD_ROOT

%{__make} \
	CC="%{__cc}" \
	ARCHFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	XMMSPLUGINDIR=$RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%doc doc/{BUGS,PLANS,UAE-*,audio_emulation.txt}
%attr(755,root,root) %{_bindir}/mod2ogg2.sh
%attr(755,root,root) %{_bindir}/uade123
%attr(755,root,root) %{_bindir}/uadefs
%attr(755,root,root) %{_bindir}/uadexmmsadd
%dir %{_libdir}/uade2
%attr(755,root,root) %{_libdir}/uade2/uadecore
%{_datadir}/uade2
%{_mandir}/man1/*
%{_pkgconfigdir}/uade.pc

%files examples
%defattr(644,root,root,755)
%doc songs/*

%files -n xmms-input-uade2
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_input_plugindir}/*.so
