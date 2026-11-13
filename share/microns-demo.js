export const micronsRecord = {
  audience:'Students at a science booth',
  theme:'Cell types and connections',
  citation:'MICrONS Consortium et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature 640, 435–447 (2025). doi:10.1038/s41586-025-08790-w',
  status:'observed',
  question:'Can we match what a brain cell does to its wiring?',
  problem:'Activity images and wiring maps answer different questions. Linking them requires recognizing the same cell in both.',
  contribution:'The team aligned images from live calcium imaging and electron microscopy using landmarks such as cell bodies and blood vessels.',
  basis:'Experts manually matched 19,181 recording regions from 14 scans to 15,439 distinct neurons. One cell could appear in several scans.',
  finding:'Matching activity to wiring made it possible to ask whether neighboring cells with similar responses are more likely to connect.',
  relevance:'Researchers can test which features of visual responses go together with a cell’s connections.',
  limit:'The dataset came from one mouse. Repeat the analysis in other mice to test how widely wiring patterns hold.',
  'e-finding':'Nature 640, p. 441, Functional–structural co-registration, and Fig. 6g–k.',
  'e-basis':'Nature 640, p. 441. Counts from the manual matching stage. See also Extended Data Fig. 4.'
};

export const micronsDraft = {
  script:'Can we match what a brain cell does to its wiring? Imagine two pictures of the same part of a mouse brain. One shows which cells respond while the mouse watches images. The other shows where the cells connect. MICrONS lined up the pictures using landmarks such as blood vessels. Experts matched 19,181 recording regions to 15,439 distinct neurons because some cells appeared in multiple scans. Now researchers can ask whether cells that respond alike are more likely to connect. The dataset came from one mouse. Ask me how you’d tell a true match from a nearby look-alike.',
  diagram:'comparison',
  poster:{
    headline:'Can we match what a brain cell does to its wiring?',
    discovery:'MICrONS linked activity and wiring for the same cells in mouse visual cortex, letting researchers compare responses with connections.',
    problem:'One image shows cells responding while a mouse watches. Another shows their wiring. To link the two, you have to find the same cell.',
    contribution:'The team lined up live calcium images and electron microscope images using landmarks such as blood vessels and cell bodies.',
    visualA:'Activity in the living mouse',
    visualB:'Wiring in the same tissue',
    finding:'Experts matched 19,181 recording regions to 15,439 distinct neurons. Some neurons appeared in multiple scans, so the counts differ.',
    relevance:'Researchers can now ask whether nearby cells that respond to similar images are more likely to connect.',
    limit:'The dataset came from one mouse. Repeat the analysis in other mice to test how widely specific wiring patterns hold.',
    invitation:'Ask me how you’d tell a true match.'
  }
};

export const micronsDOI = 'https://doi.org/10.1038/s41586-025-08790-w';
