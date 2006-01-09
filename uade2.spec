Summary:	Replayer for old amiga music file formats
Summary(pl):	Odtwarzacz starych amigowych plików muzycznych
Name:		uade2
Version:	2.00
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://zakalwe.virtuaalipalvelin.net/uade/uade2/uade-%{version}.tar.bz2
# Source0-md5:	fd669f8c7959e98e70af4f015e2ee5c6
URL:		http://zakalwe.virtuaalipalvelin.net/uade/
BuildRequires:	gtk+-devel
BuildRequires:	libao-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UADE is a replayer for old amiga music file formats. It uses an UAE
emulation of the AMIGA Hardware and a cloned m68k-assembler Amiga
delitracker API to be able to replay those tunes again on platforms
other than the original AMIGA.

%description -l pl
UADE jest odtwarzaczem starych amigowych formatów plików muzycznych.
U¿ywa emulacji sprzêtu z UAE i sklonowanego API delitrackera, by móc
odtworzyæ ponownie te melodie na platformach innych ni¿ Amiga.

%package examples
Summary:	Sample amiga tunes
Summary(pl):	Przyk³adowe melodie
Group:		Applications/Sound

%description examples
Some sample amiga tunes you can use to test if UADE works.

%description examples -l pl
Kilka przyk³adowych amigowych melodii, które mo¿na wykorzystaæ do
sprawdzenia, czy UADE dzia³a.

%package -n xmms-input-uade2
Summary:	UADE plugin for XMMS
Summary(pl):	Wtyczka dla XMMS-a wykorzystuj±ca UADE
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description -n xmms-input-uade2
For people that prefer a GUI rather than plain console apps and their
switches or those who just want to listen to their music with XMMS and
take advantage of it's features like playlists, different output,
effect and visual plugins there's also a UADE XMMS input plugin.

%description -n xmms-input-uade2 -l pl
Dla tych, którzy preferuj± GUI od aplikacji trybu tekstowego i ich
prze³±czników, lub po prostu chc± s³uchaæ muzyki u¿ywaj±c XMMS-a,
korzystaj±c z jego cech, takich jak playlisty, ró¿ne wyj¶cia, efekty i
wtyczki wizualizacyjne, jest wtyczka dla XMMS-a korzystaj±ca z UADE.

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
%doc doc/{BUGS,PLANS,UAE-*,audio_emulation.txt,eagleplayer.conf,song.conf}
%attr(755,root,root) %{_bindir}/uade123
%dir %{_libdir}/uade2
%attr(755,root,root) %{_libdir}/uade2/uadecore
%{_datadir}/uade2
%{_mandir}/man1/*

%files examples
%defattr(644,root,root,755)
%doc songs/*

%files -n xmms-input-uade2
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_input_plugindir}/*.so
