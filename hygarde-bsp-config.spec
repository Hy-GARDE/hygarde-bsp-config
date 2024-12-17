Name: hygarde-bsp-config
Version: 1.1.0
Release: 0%{?dist}
Summary: hygarde-bsp-config

License: GPL-v3
URL: https://github.com/Hy-GARDE/hygarde-bsp-config
BuildArch: noarch

BuildRequires: systemd-rpm-macros

Source0: %{name}-%{version}.tar.gz

%description
%{summary}

%prep
%autosetup

%build

%install
install -D -m 0644 79-mm-quectel-ec25.rules -t %{buildroot}%{_sysconfdir}/udev/rules.d/
install -D -m 0644 postgresql-15-batz-2.0-aquarium.repo -t %{buildroot}%{_sysconfdir}/yum.repos.d/
install -D -m 0644 systemd/afm-appli-helloworld-binding--main@.service.d/realtime.conf -t %{buildroot}%{_unitdir}/afm-appli-helloworld-binding--main@.service.d/
install -D -m 0644 systemd/init.scope.d/realtime.conf -t %{buildroot}%{_unitdir}/init.scope.d/
install -D -m 0644 systemd/system.slice.d/realtime.conf -t %{buildroot}%{_unitdir}/system.slice.d/
install -D -m 0644 systemd/user.slice.d/realtime.conf -t %{buildroot}%{_unitdir}/user.slice.d/
install -m 0644 systemd/realtime.slice %{buildroot}%{_unitdir}

%files
%{_sysconfdir}/udev/rules.d/79-mm-quectel-ec25.rules
%{_sysconfdir}/yum.repos.d/postgresql-15-batz-2.0-aquarium.repo
%{_unitdir}/afm-appli-helloworld-binding--main@.service.d/realtime.conf
%{_unitdir}/init.scope.d/realtime.conf
%{_unitdir}/system.slice.d/realtime.conf
%{_unitdir}/user.slice.d/realtime.conf
%{_unitdir}/realtime.slice

%changelog
* Mon Dec 16 2024 Louis-Baptiste Sobolewski <lb.sobolewski@iot.bzh> - 1.1.0
- Add PostgreSQL 15 repository
- Add systemd configuration to isolate CPU core 2

* Tue Jan 9 2024 Louis-Baptiste Sobolewski <lb.sobolewski@iot.bzh> - 1.0.0-7.hygarde.hummingboard_5a46cd3a.rpbatz
- Initial release
- Add udev rule to keep one ttyUSB from being used by ModemManager
