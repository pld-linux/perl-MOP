#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
Summary:	MOP::MOP - Perl extension providing a meta-object protocol for Perl modules.
Name:		perl-MOP
Version:	1.00
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/MOP/MOP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Filter
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simple and, in my opinion, powerful meta-object
protocol (MOP) for Perl5 modules.  In short, such MOP allows to I<trap
the method calls> made on an object (represented by a reference) before
they reach the original module implementing them. These method calls
are redirected to another module, called the meta-module, before their
execution. The original (legitimate) destination of the method call is
in the (base) module. Of course, one day or another, the meta-module
should perform the actual normal method call at the base level, but
it can do some nice things before or after doing that. And this is the
whole purpose of its existence.

%prep
%setup -q -n MOP-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/MOP
%{_mandir}/man3/*
