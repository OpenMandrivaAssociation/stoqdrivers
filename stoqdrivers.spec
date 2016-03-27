Summary: Fiscal driver collection
Name: stoqdrivers
Epoch: 1
Version: 1.0
Release: 1
License: LGPL
Group: System/Libraries
URL: http://www.stoq.com.br/
Source: stoqdrivers-%{version}.tar.gz
Requires: python2-zope-interface >= 3.0.1
Requires: python2-serial >= 2.2
Requires: python-kiwi >= 1.9.27
BuildRequires: python-kiwi >= 1.9.28
BuildRequires: python2-zope-interface >= 3.0.1
BuildRequires: python2-serial >= 2.2
BuildArch: noarch

%description
This is a powerful collection of device drivers written in Python and totally
focused on retail systems. Stoqdrivers also offers an unified API for devices
like fiscal printers which makes it easy to embed in many applications.

%prep
%setup -q

# installed egg is kiwi not kiwi-gtk
sed -i 's/kiwi-gtk/kiwi/' requirements.txt

%build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{python2_sitelib}/stoqdrivers
%{_datadir}/locale/*/LC_MESSAGES/stoqdrivers.mo
%{_datadir}/stoqdrivers/conf/*.ini
%{python2_sitelib}/*.egg-info
