Name:           dtc
Version:        1.2.0
Release:        1%{?dist}
Summary:        Device Tree Compiler
Group:          Development/Tools
License:        GPLv2+
URL:            http://dtc.ozlabs.org/
Source:         http://www.jdl.com/software/dtc-v%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  flex, bison

%description
The Device Tree Compiler generates flattened Open Firmware style device trees
for use with PowerPC machines that lack an Open Firmware implementation

%prep
%setup -q -n dtc-v%{version}

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr

#remove the devel stuff.
rm -rf $RPM_BUILD_ROOT/usr/include/*
rm -rf $RPM_BUILD_ROOT/usr/lib/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%{_bindir}/*

%changelog
* Thu Aug 28 2008 Josh Boyer <jwboyer@gmail.com>
- Update to latest release

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-2
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Josh Boyer <jwboyer@gmail.com>
- Update to 1.1.0

* Tue Aug 21 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Bump and rebuild

* Thu Aug 09 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Update to official 1.0.0 release

* Fri Aug 03 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Update license field

* Mon Jul 09 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Update to new snapshot

* Tue Jul 03 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Update to new snapshot
- Drop upstreamed install patch

* Fri Jun 29 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Fix packaging errors

* Thu Jun 28 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Initial packaging
