Name:           tlinux
Version:        1
Release:        1%{?dist}
Summary:        Ceph repository configuration
Group:          System Environment/Base
License:        GPLv2
URL:            http://download.tlinux.com/
Source0:        tlinux.repo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
This is just test repo

%prep

%setup -q  -c -T
install -pm 644 %{SOURCE0} .
#install -pm 644 %{SOURCE1} .

%build

%install
rm -rf %{buildroot}
#install -Dpm 644 %{SOURCE0} #    %{buildroot}/%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CEPH
%if 0%{defined suse_version}
install -dm 755 %{buildroot}/%{_sysconfdir}/zypp
install -dm 755 %{buildroot}/%{_sysconfdir}/zypp/repos.d
install -pm 644 %{SOURCE0}     %{buildroot}/%{_sysconfdir}/zypp/repos.d
%else
install -dm 755 %{buildroot}/%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0}     %{buildroot}/%{_sysconfdir}/yum.repos.d
%endif

%clean
#rm -rf %{buildroot}

%post

%postun

%files
%defattr(-,root,root,-)
#%doc GPL
%if 0%{defined suse_version}
%config(noreplace) /etc/zypp/repos.d/*
%else
%config(noreplace) /etc/yum.repos.d/*
%endif
#/etc/pki/rpm-gpg/*

%changelog
* Thu Jan 28 2021 Yifeng You <nicyou@tencent.com> - 1-1.tl3
- This is test package
