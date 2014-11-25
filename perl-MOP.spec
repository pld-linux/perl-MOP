#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	MOP
%define		pnam	MOP
%include	/usr/lib/rpm/macros.perl
Summary:	MOP::MOP - Perl extension providing a meta-object protocol for Perl modules
Summary(pl.UTF-8):	MOP::MOP - rozszerzenie Perla udostępniające modułom meta-obiektowy protokół
Name:		perl-MOP
Version:	1.00
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MOP/MOP-%{version}.tar.gz
# Source0-md5:	93c05ede1ecc9c01a385e4f21fd58382
URL:		http://search.cpan.org/dist/MOP-MOP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Filter
BuildRequires:	rsh
BuildRequires:	rshd
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simple and, in my opinion, powerful meta-object
protocol (MOP) for Perl5 modules. In short, such MOP allows to trap
the method calls made on an object (represented by a reference) before
they reach the original module implementing them. These method calls
are redirected to another module, called the meta-module, before their
execution. The original (legitimate) destination of the method call is
in the (base) module. Of course, one day or another, the meta-module
should perform the actual normal method call at the base level, but it
can do some nice things before or after doing that. And this is the
whole purpose of its existence.

%description -l pl.UTF-8
Ten moduł udostępnia modułom Perla prosty, i, zdaniem autora, o dużych
możliwościach protokół meta-obiektowy (meta-object protocol - MOP). W
skrócie, MOP pozwala na przechwytywanie wywołań metod na obiekcie
(reprezentowanym przez referencję) przed osiągnięciem oryginalnego
modułu zawierającego implementację. Te wywołania metod są przed
wykonaniem przekierowywane do innego modułu, zwanego meta-modułem.
Oryginalny cel wywołania metody jest w module bazowym. Oczywiście w
którymś momencie meta-moduł powinien wykonać normalne wywołanie metody
na poziomie podstawowym, ale przed lub po tym może robić różne rzeczy.
I to właśnie jest celem istnienia modułu MOP.

%prep
%setup -q -n MOP-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MOP
%{_mandir}/man3/*
