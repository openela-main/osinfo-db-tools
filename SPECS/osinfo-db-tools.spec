# -*- rpm-spec -*-

Summary: Tools for managing the osinfo database
Name: osinfo-db-tools
Version: 1.9.0
Release: 1%{?dist}
License: GPLv2+
Source: https://releases.pagure.io/libosinfo/%{name}-%{version}.tar.xz
URL: http://libosinfo.org/

### Patches ###

BuildRequires: meson
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
BuildRequires: libarchive-devel
BuildRequires: libsoup-devel
BuildRequires: json-glib-devel
BuildRequires: /usr/bin/pod2man
BuildRequires: python3
BuildRequires: python3-pytest
BuildRequires: python3-requests

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%prep
%autosetup -S git

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%changelog
* Thu Feb 04 2021 Danilo C. L. de Paula <ddepaula@redhat.com> - 1.9.0-1
- Resolves: rhbz#1903301 - rebase osinfo-db-tools to latest fedora's

* Sun May 31 2020 Fabiano Fidêncio <fidencio@redhat.com> - 1.8.0-1
- Resolves: rhbz#1842019 - Rebase to the latest upstream release

* Wed May 22 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-4
- Related: rhbz#1712426 - New defects found in
                          osinfo-db-tools-1.5.0-2.el8

* Wed May 22 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-3
- Resolves: rhbz#1712426 - New defects found in
                           osinfo-db-tools-1.5.0-2.el8

* Mon May 20 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-2
- Resolves: rhbz#1681879 - osinfo-db-tools changes blocked until gating
                           tests are added

* Fri May 10 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-1
- Update to 1.3.0 release
- Resolves: rhbz#1699989 - Rebase to the latest upstream release

* Wed Jun 20 2018 Daniel P. Berrangé <berrange@redhat.com> - 1.2.0-1
- Update to 1.2.0 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Daniel P. Berrange <berrange@redhat.com> - 1.1.0-1
- Update to 1.1.0 release

* Fri Jul 29 2016 Daniel P. Berrange <berrange@redhat.com> - 1.0.0-1
- Initial package after split from libosinfo (rhbz #1361594)
