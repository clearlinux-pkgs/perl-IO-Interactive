#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Interactive
Version  : 1.023
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/IO-Interactive-1.023.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/IO-Interactive-1.023.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-interactive-perl/libio-interactive-perl_1.022-1.debian.tar.xz
Summary  : 'Utilities for interactive I/O'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0
Requires: perl-IO-Interactive-license = %{version}-%{release}
Requires: perl-IO-Interactive-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
=pod
=encoding utf8
=for HTML <a href="../../actions?query=workflow%3Amacos"><img src="../../workflows/macos/badge.svg"></a>

%package dev
Summary: dev components for the perl-IO-Interactive package.
Group: Development
Provides: perl-IO-Interactive-devel = %{version}-%{release}
Requires: perl-IO-Interactive = %{version}-%{release}

%description dev
dev components for the perl-IO-Interactive package.


%package license
Summary: license components for the perl-IO-Interactive package.
Group: Default

%description license
license components for the perl-IO-Interactive package.


%package perl
Summary: perl components for the perl-IO-Interactive package.
Group: Default
Requires: perl-IO-Interactive = %{version}-%{release}

%description perl
perl components for the perl-IO-Interactive package.


%prep
%setup -q -n IO-Interactive-1.023
cd %{_builddir}
tar xf %{_sourcedir}/libio-interactive-perl_1.022-1.debian.tar.xz
cd %{_builddir}/IO-Interactive-1.023
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Interactive-1.023/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Interactive
cp %{_builddir}/IO-Interactive-1.023/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Interactive/5196def79b81230e8d1bd28ea9b2ed74007204a5
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Interactive/f5fec709320453cad16e931f7d09ac370d93f429
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Interactive.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Interactive/5196def79b81230e8d1bd28ea9b2ed74007204a5
/usr/share/package-licenses/perl-IO-Interactive/f5fec709320453cad16e931f7d09ac370d93f429

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/IO/Interactive.pm
