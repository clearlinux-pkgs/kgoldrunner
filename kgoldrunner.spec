#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kgoldrunner
Version  : 24.05.1
Release  : 69
URL      : https://download.kde.org/stable/release-service/24.05.1/src/kgoldrunner-24.05.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.1/src/kgoldrunner-24.05.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.1/src/kgoldrunner-24.05.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kgoldrunner-bin = %{version}-%{release}
Requires: kgoldrunner-data = %{version}-%{release}
Requires: kgoldrunner-license = %{version}-%{release}
Requires: kgoldrunner-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Ian Wadham <iandw.au@gmail.com>
Marco Krüger
----------------------------------------------------------------------

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kgoldrunner-24.05.1
cd %{_builddir}/kgoldrunner-24.05.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718565085
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718565085
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kgoldrunner
cp %{_builddir}/kgoldrunner-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kgoldrunner/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kgoldrunner-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kgoldrunner/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kgoldrunner-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kgoldrunner/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kgoldrunner-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kgoldrunner/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kgoldrunner-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kgoldrunner/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kgoldrunner
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kgoldrunner
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
/usr/share/kgoldrunner/system/game_GotD.txt
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
/usr/share/kgoldrunner/system/sol_GotD.txt
/usr/share/kgoldrunner/system/sol_blb.txt
/usr/share/kgoldrunner/system/sol_fd.txt
/usr/share/kgoldrunner/system/sol_kgr.txt
/usr/share/kgoldrunner/system/sol_plws.txt
/usr/share/kgoldrunner/system/sol_tute.txt
/usr/share/kgoldrunner/system/sol_tutea.txt
/usr/share/kgoldrunner/themes/README
/usr/share/kgoldrunner/themes/accessible/black-on-white-actors.svgz
/usr/share/kgoldrunner/themes/accessible/black-on-white-set.svgz
/usr/share/kgoldrunner/themes/accessible/black-on-white.png
/usr/share/kgoldrunner/themes/black-on-white.desktop
/usr/share/kgoldrunner/themes/default.desktop
/usr/share/kgoldrunner/themes/default/actors.svgz
/usr/share/kgoldrunner/themes/default/climb.wav
/usr/share/kgoldrunner/themes/default/completed.ogg
/usr/share/kgoldrunner/themes/default/death.ogg
/usr/share/kgoldrunner/themes/default/default.png
/usr/share/kgoldrunner/themes/default/dig.ogg
/usr/share/kgoldrunner/themes/default/falling.ogg
/usr/share/kgoldrunner/themes/default/gameover.ogg
/usr/share/kgoldrunner/themes/default/gold.ogg
/usr/share/kgoldrunner/themes/default/ladder.ogg
/usr/share/kgoldrunner/themes/default/set.svgz
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
/usr/share/kgoldrunner/themes/nostalgia/actors.svgz
/usr/share/kgoldrunner/themes/nostalgia/blue-actors.svgz
/usr/share/kgoldrunner/themes/nostalgia/blue-set.svgz
/usr/share/kgoldrunner/themes/nostalgia/nostalgia-blues.png
/usr/share/kgoldrunner/themes/nostalgia/nostalgia.png
/usr/share/kgoldrunner/themes/nostalgia/set.svgz
/usr/share/knsrcfiles/kgoldrunner.knsrc
/usr/share/metainfo/org.kde.kgoldrunner.appdata.xml
/usr/share/qlogging-categories6/kgoldrunner.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kgoldrunner/index.cache.bz2
/usr/share/doc/HTML/ca/kgoldrunner/index.docbook
/usr/share/doc/HTML/ca/kgoldrunner/select.png
/usr/share/doc/HTML/ca/kgoldrunner/tute008.png
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
/usr/share/package-licenses/kgoldrunner/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kgoldrunner/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kgoldrunner/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kgoldrunner/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kgoldrunner/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kgoldrunner.lang
%defattr(-,root,root,-)

