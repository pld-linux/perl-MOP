%include	/usr/lib/rpm/macros.perl
Summary:	MOP perl module
Summary(pl):	Modu³ perla MOP
Name:		perl-MOP
Version:	1.00
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MOP/MOP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Filter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MOP perl module.

%description -l pl
Modu³ perla MOP.

%prep
%setup -q -n MOP-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/MOP
%{_mandir}/man3/*
