%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define name stoqdrivers
%define version 0.9.14
%define release %mkrel 1

Summary: Fiscal driver collection
Name: %{name}
Epoch: 1
Version: %{version}
Release: %{release}
License: LGPL
Group: System/Libraries
URL: http://www.stoq.com.br/
Source: stoqdrivers-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-zope-interface >= 3.0.1, python-serial >= 2.2, python-kiwi >= 1.9.27
BuildRequires: python-kiwi >= 1.9.28
BuildArch: noarch

%description
This is a powerful collection of device drivers written in Python and totally
focused on retail systems. Stoqdrivers also offers an unified API for devices
like fiscal printers which makes it easy to embed in many applications.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{python_sitelib}/stoqdrivers
%{_datadir}/locale/*/LC_MESSAGES/stoqdrivers.mo
%{_datadir}/stoqdrivers/conf/*.ini
%{python_sitelib}/*.egg-info
