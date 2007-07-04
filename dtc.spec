Name:           dtc
Version:        0
Release:        0.3.20070703%{?dist}
Summary:        Device Tree Compiler

Group:          Development/Tools
License:        GPL
URL:            http://dtc.ozlabs.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone git://www.jdl.com/software/dtc.git; cd dtc; 
#  git checkout 8cd4196ee; rm -rf .git; cd ..; mv dtc dtc-20070703;
#  tar -czvf dtc-20070703.tar.gz dtc-20070703;
Source:         dtc-20070703.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  flex, bison

%description
The Device Tree Compiler generates flattened Open Firmware style device trees
for use with PowerPC machines that lack an Open Firmware implementation

%prep
%setup -q -n dtc-20070703

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
* Tue Jul 03 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Update to new snapshot
- Drop upstreamed install patch

* Fri Jun 29 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Fix packaging errors

* Thu Jun 28 2007 Josh Boyer <jwboyer@jdub.homelinux.org>
- Initial packaging
