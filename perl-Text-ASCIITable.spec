#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	ASCIITable
Summary:	Text::ASCIITable - Create a nice formatted table using ASCII characters
Summary(pl.UTF-8):   Text::ASCIITable - tworzenie ładne sformatowanych tabel przy użyciu znaków ASCII
Name:		perl-Text-ASCIITable
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4fb516df15271f68d0a47e4afadf83be
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::ASCIITable is a module creates a nice formatted table using
ASCII characters.

Pretty nifty if you want to output dynamic text to your console or
other fixed-size-font displays, and at the same time it will display
it in a nice human-readable, or "cool" way.

%description -l pl.UTF-8
Text::ASCIITable to moduł tworzący ładne sformatowane tabele przy
użyciu znaków ASCII.

Jest to przydatne kiedy chcemy stworzyć dynamiczny tekst na terminalu
albo innym wyjściu z fontem o stałej szerokości, jednocześnie
wyglądający ładnie i czytelnie dla człowieka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/Text/*.pm
%{perl_vendorlib}/Text/ASCIITable
%{_mandir}/man3/*
