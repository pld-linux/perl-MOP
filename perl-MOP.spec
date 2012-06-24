#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
Summary:	MOP::MOP - Perl extension providing a meta-object protocol for Perl modules
Summary(pl):	MOP::MOP - rozszerzenie Perla udost�pniaj�ce modu�om meta-obiektowy protok�
Name:		perl-MOP
Version:	1.00
Release:	8
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
protocol (MOP) for Perl5 modules.  In short, such MOP allows to trap
the method calls made on an object (represented by a reference) before
they reach the original module implementing them. These method calls
are redirected to another module, called the meta-module, before their
execution. The original (legitimate) destination of the method call is
in the (base) module. Of course, one day or another, the meta-module
should perform the actual normal method call at the base level, but it
can do some nice things before or after doing that. And this is the
whole purpose of its existence.

%description -l pl
Ten modu� udost�pnia modu�om Perla prosty, i, zdaniem autora, o du�ych
mo�liwo�ciach protok� meta-obiektowy (meta-object protocol - MOP). W
skr�cie, MOP pozwala na przechwytywanie wywo�a� metod na obiekcie
(reprezentowanym przez referencj�) przed osi�gni�ciem oryginalnego
modu�u zawieraj�cego implementacj�. Te wywo�ania metod s� przed
wykonaniem przekierowywane do innego modu�u, zwanego meta-modu�em.
Oryginalny cel wywo�ania metody jest w module bazowym. Oczywi�cie w
kt�rym� momencie meta-modu� powinien wykona� normalne wywo�anie metody
na poziomie podstawowym, ale przed lub po tym mo�e robi� r�ne rzeczy.
I to w�a�nie jest celem istnienia modu�u MOP.

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
