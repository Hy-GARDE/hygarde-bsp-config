Name: hygarde-bsp-config
Version: 1.0.0
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

%files
%{_sysconfdir}/udev/rules.d/79-mm-quectel-ec25.rules

%changelog
