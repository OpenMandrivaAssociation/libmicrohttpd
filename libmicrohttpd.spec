%define major 10
%define shortname microhttpd
%define libname	%mklibname %shortname %major
%define develname %mklibname -d %shortname

Summary:	Small C library to run an HTTP server
Name:		libmicrohttpd
Version:	0.9.22
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://gnunet.org/libmicrohttpd/
Source0:	http://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
BuildRequires:	curl-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	gnutls-devel

%description
libmicrohttpd is a small C library that is supposed to make it easy to
run an HTTP server as part of another application. Key features that
distinguish libmicrohttpd from other projects are:

* C library: fast and small
* API is simple, expressive and fully reentrant
* Implementation is (largely) http 1.1 compliant
* HTTP server can listen on multiple ports
* Support for IPv6
* Creates binary of only 22k (for now)
* Three different threading models

libmicrohttpd was started because the author needed an easy way to add
a concurrent HTTP server to other projects. Existing alternatives were
either non-free, not reentrant, standalone, of terrible code quality or
a combination thereof. Do not use libmicrohttpd if you are looking for
a standalone http server; there are many other projects out there that
provide that kind of functionality already. However, if you want to be
able to serve simple WWW pages from within your C or C++ application,
check it out.

%package -n %libname
Summary:	Small C library to run an HTTP server
Group:		System/Libraries

%description -n %libname
libmicrohttpd is a small C library that is supposed to make it easy to
run an HTTP server as part of another application. Key features that
distinguish libmicrohttpd from other projects are:

* C library: fast and small
* API is simple, expressive and fully reentrant
* Implementation is (largely) http 1.1 compliant
* HTTP server can listen on multiple ports
* Support for IPv6
* Creates binary of only 22k (for now)
* Three different threading models

libmicrohttpd was started because the author needed an easy way to add
a concurrent HTTP server to other projects. Existing alternatives were
either non-free, not reentrant, standalone, of terrible code quality or
a combination thereof. Do not use libmicrohttpd if you are looking for
a standalone http server; there are many other projects out there that
provide that kind of functionality already. However, if you want to be
able to serve simple WWW pages from within your C or C++ application,
check it out.

%package -n %develname
Summary:	Development files for %libname
Group:		System/Libraries
Provides:	%name-devel = %{EVRD}
Requires:	%{libname} = %{version}

%description -n %develname
Development files for %libname

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%if %{mdvver} < 201200

%post -n %develname
%_install_info microhttpd.info

%preun -n %develname
%_remove_install_info microhttpd.info

%endif

%files -n %libname
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{name}.so.%{major}*
%{_mandir}/man3/%{name}.3.*

%files -n %develname
%{_includedir}/%{shortname}.h
%{_libdir}/%{name}.so
%{_datadir}/info/*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Sep 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.22-1
+ Revision: 816597
- update to 0.9.22

* Mon Jul 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.21-1
+ Revision: 810683
- update to 0.9.21
- disable building static libs
- specfile cleanup

* Thu Nov 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.16-1
+ Revision: 731338
- 0.9.16

* Thu Jun 23 2011 Funda Wang <fwang@mandriva.org> 0.9.12-1
+ Revision: 686820
- update to new version 0.9.12

* Sat May 21 2011 Funda Wang <fwang@mandriva.org> 0.9.11-1
+ Revision: 676512
- update to new version 0.9.11

* Wed Apr 27 2011 Funda Wang <fwang@mandriva.org> 0.9.10-1
+ Revision: 659688
- update to new version 0.9.10

* Sun Mar 06 2011 Funda Wang <fwang@mandriva.org> 0.9.8-1
+ Revision: 642213
- update to new version 0.9.8

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 0.9.6-1
+ Revision: 634086
- update to new version 0.9.6

* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 0.9.4-1mdv2011.0
+ Revision: 625192
- new version 0.9.4

* Sat Sep 11 2010 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2011.0
+ Revision: 577146
- new version 0.9.1

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.9.0-1mdv2011.0
+ Revision: 560900
- New version 0.9.0

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 0.4.6-1mdv2010.1
+ Revision: 518686
- new version 0.4.6

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 0.4.5-1mdv2010.1
+ Revision: 504694
- new version 0.4.5

* Sun Nov 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 463098
- update to new version 0.4.3

* Wed Sep 09 2009 Lev Givon <lev@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 436073
- Update to 0.4.2.

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-3mdv2010.0
+ Revision: 429810
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-2mdv2009.0
+ Revision: 267893
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 212197
- New version 0.3.1

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2008.1
+ Revision: 161659
- update to new version 0.2.1

* Fri Dec 28 2007 Nicolas Vigier <nvigier@mandriva.com> 0.2.0-1mdv2008.1
+ Revision: 138879
- new version

* Tue Dec 18 2007 Nicolas Vigier <nvigier@mandriva.com> 0.1.2-1mdv2008.1
+ Revision: 132256
- new version

* Mon Aug 20 2007 Nicolas Vigier <nvigier@mandriva.com> 0.0.3-1mdv2008.0
+ Revision: 67318
- new version 0.0.3

* Tue Aug 14 2007 Nicolas Vigier <nvigier@mandriva.com> 0.0.1-1mdv2008.0
+ Revision: 63406
- Import libmicrohttpd

