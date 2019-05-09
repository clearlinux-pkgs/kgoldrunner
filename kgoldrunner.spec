#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kgoldrunner
Version  : 19.04.1
Release  : 9
URL      : https://download.kde.org/stable/applications/19.04.1/src/kgoldrunner-19.04.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.1/src/kgoldrunner-19.04.1.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.1/src/kgoldrunner-19.04.1.tar.xz.sig
Summary  : A game of action and puzzle solving
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kgoldrunner-bin = %{version}-%{release}
Requires: kgoldrunner-data = %{version}-%{release}
Requires: kgoldrunner-license = %{version}-%{release}
Requires: kgoldrunner-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
THEMES IN KGOLDRUNNER
For each pictorial theme in KGoldrunner there is a "*.desktop" file in the area
kdegames/kgoldrunner/themes in the KDE SVN source-code repository, or in the
area $HOME/.kde/share/apps/kgoldrunner/themes, the user's local data area.  If
two *.desktop files have the same name, the one in the local area takes
precedence.

%package bin
Summary: bin components for the kgoldrunner package.
Group: Binaries
Requires: kgoldrunner-data = %{version}-%{release}
Requires: kgoldrunner-license = %{version}-%{release}

%description bin
bin components for the kgoldrunner package.


%package data
Summary: data components for the kgoldrunner package.
Group: Data

%description data
data components for the kgoldrunner package.


%package doc
Summary: doc components for the kgoldrunner package.
Group: Documentation

%description doc
doc components for the kgoldrunner package.


%package license
Summary: license components for the kgoldrunner package.
Group: Default

%description license
license components for the kgoldrunner package.


%package locales
Summary: locales components for the kgoldrunner package.
Group: Default

%description locales
locales components for the kgoldrunner package.


%prep
%setup -q -n kgoldrunner-19.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557442228
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557442228
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kgoldrunner
cp COPYING %{buildroot}/usr/share/package-licenses/kgoldrunner/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kgoldrunner/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang kgoldrunner

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kgoldrunner

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kgoldrunner.desktop
/usr/share/icons/hicolor/128x128/apps/kgoldrunner.png
/usr/share/icons/hicolor/16x16/apps/kgoldrunner.png
/usr/share/icons/hicolor/22x22/apps/kgoldrunner.png
/usr/share/icons/hicolor/32x32/apps/kgoldrunner.png
/usr/share/icons/hicolor/48x48/apps/kgoldrunner.png
/usr/share/icons/hicolor/64x64/apps/kgoldrunner.png
/usr/share/kgoldrunner/system/game_CM.txt
/usr/share/kgoldrunner/system/game_GMEP.txt
/usr/share/kgoldrunner/system/game_GMGR.txt
/usr/share/kgoldrunner/system/game_GRII.txt
/usr/share/kgoldrunner/system/game_MAZ.txt
/usr/share/kgoldrunner/system/game_blb.txt
/usr/share/kgoldrunner/system/game_cnt.txt
/usr/share/kgoldrunner/system/game_ende.txt
/usr/share/kgoldrunner/system/game_fd.txt
/usr/share/kgoldrunner/system/game_kgr.txt
/usr/share/kgoldrunner/system/game_lars.txt
/usr/share/kgoldrunner/system/game_plws.txt
/usr/share/kgoldrunner/system/game_plwv.txt
/usr/share/kgoldrunner/system/game_sot.txt
/usr/share/kgoldrunner/system/game_tute.txt
/usr/share/kgoldrunner/system/game_tutea.txt
/usr/share/kgoldrunner/system/game_wad.txt
/usr/share/kgoldrunner/system/hi_kgr.dat
/usr/share/kgoldrunner/system/hi_plws.dat
/usr/share/kgoldrunner/system/hi_plwv.dat
/usr/share/kgoldrunner/system/hi_wad.dat
/usr/share/kgoldrunner/system/rec_GMGR.txt
/usr/share/kgoldrunner/system/rec_GRII.txt
/usr/share/kgoldrunner/system/rec_demo.txt
/usr/share/kgoldrunner/system/sol_blb.txt
/usr/share/kgoldrunner/system/sol_fd.txt
/usr/share/kgoldrunner/system/sol_kgr.txt
/usr/share/kgoldrunner/system/sol_plws.txt
/usr/share/kgoldrunner/system/sol_tute.txt
/usr/share/kgoldrunner/system/sol_tutea.txt
/usr/share/kgoldrunner/themes/README
/usr/share/kgoldrunner/themes/accessible/black-on-white-actors.svg
/usr/share/kgoldrunner/themes/accessible/black-on-white-set.svg
/usr/share/kgoldrunner/themes/accessible/black-on-white.png
/usr/share/kgoldrunner/themes/black-on-white.desktop
/usr/share/kgoldrunner/themes/default.desktop
/usr/share/kgoldrunner/themes/default/actors.svg
/usr/share/kgoldrunner/themes/default/climb.wav
/usr/share/kgoldrunner/themes/default/completed.ogg
/usr/share/kgoldrunner/themes/default/death.ogg
/usr/share/kgoldrunner/themes/default/default.png
/usr/share/kgoldrunner/themes/default/dig.ogg
/usr/share/kgoldrunner/themes/default/falling.ogg
/usr/share/kgoldrunner/themes/default/gameover.ogg
/usr/share/kgoldrunner/themes/default/gold.ogg
/usr/share/kgoldrunner/themes/default/ladder.ogg
/usr/share/kgoldrunner/themes/default/set.svg
/usr/share/kgoldrunner/themes/default/step.wav
/usr/share/kgoldrunner/themes/default/victory.ogg
/usr/share/kgoldrunner/themes/egypt.desktop
/usr/share/kgoldrunner/themes/egypt/actors.svgz
/usr/share/kgoldrunner/themes/egypt/egypt.png
/usr/share/kgoldrunner/themes/egypt/egypt_kgr.svgz
/usr/share/kgoldrunner/themes/kgr_geek.desktop
/usr/share/kgoldrunner/themes/kgr_geek/actors.svgz
/usr/share/kgoldrunner/themes/kgr_geek/kgr_geek.png
/usr/share/kgoldrunner/themes/kgr_geek/set.svgz
/usr/share/kgoldrunner/themes/nostalgia-blues.desktop
/usr/share/kgoldrunner/themes/nostalgia.desktop
/usr/share/kgoldrunner/themes/nostalgia/actors.svg
/usr/share/kgoldrunner/themes/nostalgia/blue-actors.svg
/usr/share/kgoldrunner/themes/nostalgia/blue-set.svg
/usr/share/kgoldrunner/themes/nostalgia/nostalgia-blues.png
/usr/share/kgoldrunner/themes/nostalgia/nostalgia.png
/usr/share/kgoldrunner/themes/nostalgia/set.svg
/usr/share/kxmlgui5/kgoldrunner/kgoldrunnerui.rc
/usr/share/metainfo/org.kde.kgoldrunner.appdata.xml
/usr/share/xdg/kgoldrunner.categories
/usr/share/xdg/kgoldrunner.knsrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kgoldrunner/editbar.png
/usr/share/doc/HTML/de/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/de/kgoldrunner/index.docbook
/usr/share/doc/HTML/de/kgoldrunner/select.png
/usr/share/doc/HTML/de/kgoldrunner/tute008.png
/usr/share/doc/HTML/en/kgoldrunner/editbar.png
/usr/share/doc/HTML/en/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/en/kgoldrunner/index.docbook
/usr/share/doc/HTML/en/kgoldrunner/select.png
/usr/share/doc/HTML/en/kgoldrunner/tute008.png
/usr/share/doc/HTML/es/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/es/kgoldrunner/index.docbook
/usr/share/doc/HTML/et/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/et/kgoldrunner/index.docbook
/usr/share/doc/HTML/fr/kgoldrunner/editbar.png
/usr/share/doc/HTML/fr/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/fr/kgoldrunner/index.docbook
/usr/share/doc/HTML/fr/kgoldrunner/select.png
/usr/share/doc/HTML/fr/kgoldrunner/tute008.png
/usr/share/doc/HTML/gl/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/gl/kgoldrunner/index.docbook
/usr/share/doc/HTML/it/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/it/kgoldrunner/index.docbook
/usr/share/doc/HTML/nl/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/nl/kgoldrunner/index.docbook
/usr/share/doc/HTML/pt/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/pt/kgoldrunner/index.docbook
/usr/share/doc/HTML/pt_BR/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kgoldrunner/index.docbook
/usr/share/doc/HTML/sv/kgoldrunner/editbar.png
/usr/share/doc/HTML/sv/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/sv/kgoldrunner/index.docbook
/usr/share/doc/HTML/sv/kgoldrunner/select.png
/usr/share/doc/HTML/sv/kgoldrunner/tute008.png
/usr/share/doc/HTML/uk/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/uk/kgoldrunner/index.docbook
/usr/share/doc/HTML/uk/kgoldrunner/select.png
/usr/share/doc/HTML/uk/kgoldrunner/tute008.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kgoldrunner/COPYING
/usr/share/package-licenses/kgoldrunner/COPYING.DOC

%files locales -f kgoldrunner.lang
%defattr(-,root,root,-)

