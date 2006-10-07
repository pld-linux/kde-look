Summary:	www.kde-look.org resources
Summary(pl):	Zasoby www.kde-look.org
Name:		kde-look
Version:	1
Release:	1
License:	GPL (?)
Group:		Themes

# Wallpapers 800x600
# Other
Source0:	http://students.fh-joanneum.at/hoffer/art9/rotane_qubiq_room_0800.jpg
# Source0-md5:	6227dd4edfde477310b6fa2dda14fb91
Source1:	http://www.kde-look.org/content/files/546-transport_vi.jpg
# Source1-md5:	433c07e95ea598bb53d6b703bc352d54
# KDE
Source2:	http://www.kde-look.org/content/files/3515-iceage_kde_800.jpg
# Source2-md5:	a9321df50b87c1be5579beba8b906f6d

# Wallpapers 1024x768
# Other
Source5:	http://www.kde-look.org/content/files/15000-Unwetterhimmel.jpg
# Source5-md5:	0c3cf1c13486159b5ebc7c2070c1a1d4
# TUX
Source3:	http://www.kde-look.org/content/files/10434-tuxwinv02.tgz
# Source3-md5:	7ea1d4429a057073eb80015addcd0321
#PLD
Source4:	http://www.kde-look.org/content/files/12955-pld-greenwallpaper.png
# Source4-md5:	0637c81dc2f3e91f5751d028b86e7d80

URL:		http://www.kde-look.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
www.kde-look.org resources.

%description -l pl
Zasoby www.kde-look.org .

#Wallpapers
#Other
%package wallpapers-other-800x600
Summary:	Wallpapers
Summary(pl):	Tapety
Group:		Themes
Requires:	kdelibs

%description wallpapers-other-800x600
800x600 resolution wallpapers.

%description wallpapers-other-800x600 -l pl
Tapety w rozdzielczo¶ci 800x600.

%package wallpapers-other-1024x768
Summary:	Wallpapers
Summary(pl):	Tapety
Group:		Themes
Requires:	kdelibs

%description wallpapers-other-1024x768
1024x768 resolution wallpapers.

%description wallpapers-other-1024x768 -l pl
Tapety w rozdzielczo¶ci 1024x768.

#KDE
%package wallpapers-kde-800x600
Summary:	Wallpapers
Summary(pl):	Tapety
Group:		Themes
Requires:	kdelibs

%description wallpapers-kde-800x600
800x600 resolution wallpapers.

%description wallpapers-kde-800x600 -l pl
Tapety w rozdzielczo¶ci 800x600.

#TUX
%package wallpapers-tux-1024x768
Summary:	Wallpapers
Summary(pl):	Tapety
Group:		Themes
Requires:	kdelibs

%description wallpapers-tux-1024x768
1024x768 resolution wallpapers.

%description wallpapers-tux-1024x768 -l pl
Tapety w rozdzielczo¶ci 1024x768.

%package wallpapers-tux-1280x1024
Summary:	Wallpapers
Summary(pl):	Tapety
Group:		Themes
Requires:	kdelibs

%description wallpapers-tux-1280x1024
1280x1024 resolution wallpapers.

%description wallpapers-tux-1280x1024 -l pl
Tapety w rozdzielczo¶ci 1280x1024.

%package wallpapers-tux-1600x1200
Summary:	Wallpapers
Summary(pl):	Tapety
Group:		Themes
Requires:	kdelibs

%description wallpapers-tux-1600x1200
1600x1200 resolution wallpapers.

%description wallpapers-tux-1600x1200 -l pl
Tapety w rozdzielczo¶ci 1600x1200.

#PLD
%package wallpapers-pld-1024x768
Summary:	Wallpapers
Summary(pl):	Tapety
Group:		Themes
Requires:	kdelibs

%description wallpapers-pld-1024x768
1024x768 resolution wallpapers.

%description wallpapers-pld-1024x768 -l pl
Tapety w rozdzielczo¶ci 1024x768.

%prep
%setup -Tc -n %{name}-%{version} -b3

%build

%install
%define destdir $RPM_BUILD_ROOT%{_datadir}/wallpapers
install -d %{destdir}

cp %{SOURCE0} %{destdir}/Other-qubiq-room-800x600.jpg
cp %{SOURCE1} %{destdir}/Other-Linux-electron-800x600.jpg
cp %{SOURCE5} %{destdir}/Other-Unwetterhimmel-1024x768.jpg

cp %{SOURCE2} %{destdir}/KDE-IceAge-800x600.jpg

cp tuxwinv02/*1024x768* %{destdir}/TUX-tuxwin-1024x768.jpg
cp tuxwinv02/*1280x1024* %{destdir}/TUX-tuxwin-1280x1024.jpg
cp tuxwinv02/*1600x1200* %{destdir}/TUX-tuxwin-1600x1200.jpg

cp %{SOURCE4} %{destdir}/PLD-green-1024x768.jpg

%clean
rm -rf $RPM_BUILD_ROOT

#Wallpapers
#Other
%files wallpapers-other-800x600
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Other-*-800x600.jpg

%files wallpapers-other-1024x768
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Other-*-1024x768.jpg

#KDE
%files wallpapers-kde-800x600
%defattr(644,root,root,755)
%{_datadir}/wallpapers/KDE-*-800x600.jpg

#TUX
%files wallpapers-tux-1024x768
%defattr(644,root,root,755)
%{_datadir}/wallpapers/TUX-*-1024x768.jpg

%files wallpapers-tux-1280x1024
%defattr(644,root,root,755)
%{_datadir}/wallpapers/TUX-*-1280x1024.jpg

%files wallpapers-tux-1600x1200
%defattr(644,root,root,755)
%{_datadir}/wallpapers/TUX-*-1600x1200.jpg

#PLD
%files wallpapers-pld-1024x768
%defattr(644,root,root,755)
%{_datadir}/wallpapers/PLD-*-1024x768.jpg
