Name: hygarde-bsp-config
Version: 1.1.0
Release: 7%{?dist}
Summary: hygarde-bsp-config

License: GPL-v3
URL: https://github.com/Hy-GARDE/hygarde-bsp-config
BuildArch: noarch

Source0: %{name}-%{version}.tar.gz

%description
%{summary}

%prep
%autosetup

%build

%install
install -d %{buildroot}%{_sysconfdir}/udev/rules.d
install -m 0644 79-mm-quectel-ec25.rules %{buildroot}%{_sysconfdir}/udev/rules.d/
install -m 0644 postgresql-15-batz-2.0-aquarium.repo %{buildroot}%{_sysconfdir}/yum.repos.d/

%files
%{_sysconfdir}/udev/rules.d/79-mm-quectel-ec25.rules
%{_sysconfdir}/yum.repos.d/postgresql-15-batz-2.0-aquarium.repo

%changelog
