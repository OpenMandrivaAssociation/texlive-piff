# revision 21894
# category Package
# catalog-ctan /macros/latex/contrib/piff
# catalog-date 2010-12-08 08:17:08 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-piff
Version:	20101208
Release:	1
Summary:	Macro tools by Mike Piff
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/piff
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piff.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piff.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The set consists (now) of: - a small package for dealing with
duplicate-numbered output pages; - newproof, for defining
mathematical proof structures; - onepagem for omitting the page
number in one-page documents and - time, which prints a 12-hour
format time.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
