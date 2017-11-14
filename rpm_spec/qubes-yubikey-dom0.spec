%{!?version: %define version %(cat version)}

Name:		qubes-yubikey-dom0
Version:    %{version}
Release:	1%{?dist}
Summary:	Yubikey support scripts for Qubes OS

Group:		Applications/System
License:	GPL
URL:		https://www.qubes-os.org/doc/yubi-key/

Requires:	openssl

%if 0%{?qubes_builder}
%define _builddir %(pwd)
%endif

%description
Scripts for easier integration of YubiKey into Qubes OS login.

%prep
%if ! 0%{?qubes_builder}
%setup -q
%endif

%build

%install
cp -a etc $RPM_BUILD_ROOT/
mkdir $RPM_BUILD_ROOT/usr
cp -a bin $RPM_BUILD_ROOT/usr/

%files
%doc README.md
%config(noreplace) /etc/pam.d/yubico
%config(noreplace) /etc/qubes/yk-keys/yk-vm
%config(noreplace) /etc/qubes/yk-keys/yk-login-pass
%config(noreplace) /etc/qubes/yk-keys/yk-login-pass-hashed.hex
%config(noreplace) /etc/qubes/yk-keys/yk-secret-key.hex
/usr/bin/yk-auth

%changelog

