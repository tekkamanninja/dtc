Name:           dtc
Version:        0
Release:        0.4.20070709%{?dist}
Summary:        Device Tree Compiler

Group:          Development/Tools
License:        GPL
URL:            http://dtc.ozlabs.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone git://www.jdl.com/software/dtc.git; cd dtc; 
#  git checkout fdd2e6f9; rm -rf .git; cd ..; mv dtc dtc-20070709;
#  tar -czvf dtc-20070709.tar.gz dtc-20070709;
Source:         dtc-20070709.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  flex, bison

%description
The Device Tree Compiler generates flattened Open Firmware style device trees
for use with PowerPC machines that lack an Open Firmware implementation

%prep
%setup -q -n dtc-20070709

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%{_bindir}/*

%changelog
* Mon Jul 09 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Update to new snapshot

* Tue Jul 03 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Update to new snapshot
- Drop upstreamed install patch

* Fri Jun 29 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Fix packaging errors

* Thu Jun 28 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Initial packaging
