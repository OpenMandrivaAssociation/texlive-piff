Name:		texlive-piff
Version:	21894
Release:	1
Summary:	Macro tools by Mike Piff
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/piff
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piff.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The set consists (now) of: - a small package for dealing with
duplicate-numbered output pages; - newproof, for defining
mathematical proof structures; - onepagem for omitting the page
number in one-page documents and - time, which prints a 12-hour
format time.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/piff/duplicat.sty
%{_texmfdistdir}/tex/latex/piff/newproof.sty
%{_texmfdistdir}/tex/latex/piff/onepagem.sty
%{_texmfdistdir}/tex/latex/piff/time.sty
%doc %{_texmfdistdir}/doc/latex/piff/README
%doc %{_texmfdistdir}/doc/latex/piff/duplicat-doc.pdf
%doc %{_texmfdistdir}/doc/latex/piff/duplicat-doc.tex
%doc %{_texmfdistdir}/doc/latex/piff/newproof-doc.pdf
%doc %{_texmfdistdir}/doc/latex/piff/newproof-doc.tex
%doc %{_texmfdistdir}/doc/latex/piff/onepagem-doc.pdf
%doc %{_texmfdistdir}/doc/latex/piff/onepagem-doc.tex
%doc %{_texmfdistdir}/doc/latex/piff/time-doc.pdf
%doc %{_texmfdistdir}/doc/latex/piff/time-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
